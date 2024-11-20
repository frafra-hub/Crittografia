from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64

with open ('private_key.pem', 'rb') as key_file:
    private_key=serialization.load_pem_private_key(key_file.read(),password=None)

with open ('public_key.pem', 'rb') as key_file:
    public_key=serialization.load_pem_public_key(key_file.read())

message='Ciao, Epicode spacca!'

encrypted= public_key.encrypt(message.encode(), padding.PKCS1v15())

decypted=private_key.decrypt(encrypted, padding.PKCS1v15())

print ("Messaggio originale: ",message)
print ("Messaggio criptato: ", base64.b64encode(encrypted).decode('utf-8'))
print ("Messaggio decriptato: ", decypted.decode('utf-8'))
