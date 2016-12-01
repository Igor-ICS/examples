from Crypto.Cipher import AES
from Crypto import Random
import sys

def genKey():
	return Random.new().read(16)

def encrypt(key, text):
	iv = Random.new().read(AES.block_size)
	return (iv,AES.new(key, AES.MODE_CFB, iv).encrypt(text))

if __name__ == "__main__":
	key = genKey()
	print encrypt(key, ''.join(sys.argv[1:]))