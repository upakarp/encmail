def encrypt_this(text,key):
	new_text = ""
	tlength = len(text)
	klength = len(key)
	for i in range(0, tlength):
		m = i % klength
		a = text[i]
		b = key[m]
		c = chr(ord(a)+ord(b))
		new_text = new_text + c
	return new_text

def decrypt_this(text,key):
	new_text = ""
	tlength = len(text)
	klength = len(key)
	for i in range(0, tlength):
		m = i % klength
		a = text[i]
		b = key[m]
		c = chr(ord(a)-ord(b))
		new_text = new_text + c
	return new_text