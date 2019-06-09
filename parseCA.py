
import base64
from OpenSSL import crypto
from test.support import get_attribute
import asn1
import chardet
file_folder="D:\\WorkSpace\\Tools\\certificateFiles\\"
filename="lukagao_root.cer"
path=file_folder+filename
certbuffer=''
with open(path,'rb') as f:
    certbuffer=f.read()

#print certbuffer.encode("ascii")

cert=crypto.load_certificate(crypto.FILETYPE_ASN1, certbuffer)
subject=cert.get_subject()
pubk=cert.get_pubkey()
keybuffer=crypto.dump_publickey(crypto.FILETYPE_PEM, pubk)
print keybuffer
certstr=crypto.dump_certificate(crypto.FILETYPE_ASN1, cert)
print certbuffer
#data = base64.decodestring(s)
#print data


'''
decoder = asn1.Decoder()
decoder.start(certbuffer)
tag, value = decoder.read()
print tag,value.encode("ascii")
'''