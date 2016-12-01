import hashlib, sys

def MD5(arg):
	print 'MD5:    '+hashlib.md5(''.join(arg[1:])).hexdigest()
	return

def SHA1(arg):
	print 'SHA1:   '+ hashlib.sha1(''.join(arg[1:])).hexdigest()
	return

def SHA256(arg):
	print 'SHA256: '+ hashlib.sha256(''.join(arg[1:])).hexdigest()
	return

def SHA512(arg):
	print 'SHA512: '+ hashlib.sha512(''.join(arg[1:])).hexdigest()
	return

def bcrypt():
	return

def run(args):
	mode = args[0].upper()
	if mode == 'MD5':
		MD5(args[1:])
	elif mode == 'SHA1':
		SHA1(args[1:])
	elif mode == 'SHA256':
		SHA256(args[1:])
	elif mode == 'SHA512':
		SHA512(args[1:])
	elif mode == 'BCRYPT':
		bcrypt(args[1:])
	elif mode == 'ALL':
		MD5(args[1:])
		SHA1(args[1:])
		SHA256(args[1:])
		SHA512(args[1:])
	else:
		print str(''.join(args[1:]))
		print "Wrong arguments"

if __name__ == "__main__":
   run(sys.argv[1:])