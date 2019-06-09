import time
from M2Crypto import X509, EVP, RSA, ASN1

KeyLength=2048

CAName='TS.CN'               
ServerName='CF.CN'

CAKeyFile='ca.key'
CACerFile='ca.cer'
ServerKeyFile='server.key'
ServerCerFile='Server.cer'


def mk_ca_issuer():
    """
    Our default CA issuer name.
    """
    issuer = X509.X509_Name()
    issuer.C = 'CN'
    issuer.CN = CAName
    issuer.ST = 'TS'
    issuer.L = 'TS'
    issuer.O = 'TS'
    issuer.OU = 'TS'
    return issuer


def mk_cert_valid(cert, days=365):
    """
    Make a cert valid from now and til 'days' from now.
    Args:
       cert -- cert to make valid
       days -- number of days cert is valid for from now.
    """
    t = long(time.time())
    now = ASN1.ASN1_UTCTIME()
    now.set_time(t)
    expire = ASN1.ASN1_UTCTIME()
    expire.set_time(t + days * 24 * 60 * 60)
    cert.set_not_before(now)
    cert.set_not_after(expire)


def mk_request(bits, cn='CF.CN'):
    """
    Create a X509 request with the given number of bits in they key.
    Args:
      bits -- number of RSA key bits
      cn -- common name in the request
    Returns a X509 request and the private key (EVP)
    """
    pk = EVP.PKey()
    x = X509.Request()
    rsa = RSA.gen_key(bits, 65537, lambda: None)
    pk.assign_rsa(rsa)
    x.set_pubkey(pk)
    name = x.get_subject()
    name.C = 'CN'
    name.CN = cn
    name.ST = 'TS'
    name.O = 'TS'
    name.OU = 'TS'
    x.sign(pk,'sha1')
    return x, pk


def mk_cacert():
    """
    Make a CA certificate.
    Returns the certificate, private key and public key.
    """
    req, pk = mk_request(KeyLength)
    pkey = req.get_pubkey()
    cert = X509.X509()
    cert.set_serial_number(1)
    cert.set_version(2)
    mk_cert_valid(cert)
    cert.set_issuer(mk_ca_issuer())
    cert.set_subject(cert.get_issuer())
    cert.set_pubkey(pkey)
    cert.add_ext(X509.new_extension('basicConstraints', 'CA:TRUE'))
    cert.add_ext(X509.new_extension('subjectKeyIdentifier', cert.get_fingerprint()))
    cert.sign(pk, 'sha1')
    return cert, pk, pkey


def mk_cert():
    """
    Make a certificate.
    """
    cert = X509.X509()
    cert.set_serial_number(2)
    cert.set_version(2)
    mk_cert_valid(cert)
    cert.add_ext(X509.new_extension('nsComment', 'SSL sever'))
    return cert


def mk_casigned_cert():
    """
    Create a CA cert + server cert + server private key.
    """
    # unused, left for history.
    cacert, pk1, _ = mk_cacert()
    cert_req, pk2 = mk_request(KeyLength, cn=ServerName)
    cert = mk_cert()
    cert.set_issuer(cacert.get_issuer())
    cert.set_subject(cert_req.get_subject())
    cert.set_pubkey(cert_req.get_pubkey())
    cert.sign(pk1, 'sha1')
    return cacert, cert,pk1, pk2


if __name__ == '__main__':
    cacert, cert, pk1,pk2 = mk_casigned_cert()
      
    with open(CACerFile, 'w') as f:
        f.write(cacert.as_pem())
    with open(ServerCerFile, 'w') as f:
        f.write(cert.as_pem())
    with open(CAKeyFile, 'w') as f:
        f.write(pk1.as_pem(None))
    with open(ServerKeyFile, 'w') as f:
        f.write(pk2.as_pem(None))
      
    # Sanity checks...
    cac = X509.load_cert(CACerFile)
    print cac.verify(), cac.check_ca()
    cc = X509.load_cert(ServerCerFile)
    print cc.verify(cac.get_pubkey())
