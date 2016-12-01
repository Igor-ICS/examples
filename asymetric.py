from Crypto.PublicKey import RSA
from Crypto import Random
import sys, hashlib

def genKey():
	print 'Generating key pair'
	key = RSA.generate(2048, Random.new().read)
	return key

def encrypt(key, text):
	pubKey = key.publickey()
	cipherText = pubKey.encrypt(text, 32)
	return cipherText

def decrypt(key, ciphertext):
	return key.decrypt(ciphertext)


def genHash(text):
	return hashlib.sha256(text).hexdigest()

def sign(key, text):
	hash = genHash(text)
	return key.sign(hash,'')

def verify(key, signature, text):
	hash = genHash(text)
	return key.publickey().verify(hash, signature)

if __name__ == "__main__":
	key = genKey()
	print '-------------------------------------------------------------------------------'
	ciphertext = encrypt(key, ' '.join(sys.argv[1:]))
	print 'Ciphertext: \n'+str(ciphertext[0])
	print '-------------------------------------------------------------------------------'
	plaintext = decrypt(key, ciphertext)
	print 'Decrypted text: \n'+plaintext
	print '-------------------------------------------------------------------------------'
	signature = sign(key, plaintext)
	print 'Signature: \n'+str(signature)
	print '-------------------------------------------------------------------------------'
	print verify(key, signature, plaintext)