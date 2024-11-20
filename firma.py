from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64

with open ('private_key.pem','rb') as key_file:
    private_key=serialization.load_pem_private_key(key_file.read(),password=None)

with open ('public_key.pem','rb') as key_file:
    public_key=serialization.load_pem_public_key(key_file.read())

message='Ciao, Epicode spacca!'

signed=private_key.sign(message.encode(),padding.PKCS1v15(),hashes.SHA256())
try:
    encrypted_b64=base64.b64encode(signed).decode('utf-8')
    public_key.verify(signed,message.encode(),padding.PKCS1v15(),hashes.SHA256())
    print ("Base64 della firma: ", encrypted_b64)
    print("Messaggio originale da confrontare: ", message)
    print ("La firma è valida.")
except Exception as e:
    print ("La firma non è valida.",str(e))
