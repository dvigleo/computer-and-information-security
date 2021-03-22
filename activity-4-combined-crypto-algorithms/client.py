"""
Activity 4 - Combined Crypto Algorithms
---------------------------------------
Course: Computer and Information Security
Teacher: Jorge Rodríguez Ruiz
Authors:
    - Daniela Vignau (A01021698)
    - Carlos García (A01025948)
    - Héctor Reyes (A01339607)
Date: 2021-03-26
"""


from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import hashlib
import socket

# Connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plaintext = b"Hello!RSA-AES"
s.connect(("54.226.141.110", 13337))

# Send first message and receive public key
s.send(plaintext)
print(f"-> {plaintext}\n")
response = s.recv(1024).decode("ascii")
print(f"<- {response}\n")

public_key = RSA.import_key(response)
rsa_instance = PKCS1_OAEP.new(public_key)

aes_key = b"abcdefgh12345678"
aes_iv = b"abcdefgh12345678"
concat = aes_key + b"," + aes_iv
ciphertext = rsa_instance.encrypt(concat)

aes_dec = AES.new(aes_key, AES.MODE_CBC, aes_iv)
aes_enc = AES.new(aes_key, AES.MODE_CBC, aes_iv)

# Send RSA-encrypted key and initialization vector and decrypt received message using AES
s.send(ciphertext)
print(f"-> {ciphertext}\n")
response = s.recv(1024)
plaintext = aes_dec.decrypt(response).decode("ascii")
print(f"<- {plaintext}\n")

# Obtain SHA256 of team, create MAC, and encrypt message using AES
team = b"DaniCarlosHector"
digest = hashlib.sha256()
digest.update(b"".join([aes_key, team]))
mac = digest.digest()
message = b"".join([team, mac])
ciphertext = aes_enc.encrypt(message)

# Decrypt received message using AES
s.send(ciphertext)
print(f"-> {ciphertext}\n")
response = s.recv(1024)
plaintext = aes_dec.decrypt(response).decode("ascii")
print(f"<- {plaintext}\n")

s.close()
