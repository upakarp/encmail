from tkinter import Tk, Label
import sqlite3
from encrypt_decrypt import *

def inbox_mail_tk(mail_id):
	wind = Tk()
	wind.minsize(300,400)

	connect = sqlite3.connect("encmailtest.db")
	result = connect.execute("SELECT from_id,to_id,sub,mail,session_key from mail where id=?",[mail_id])
	for data in result:
		fromId = data[0]
		toId = data[1]
		sub = data[2]
		mail = data[3]
		s_key = data[4]

	query = connect.execute("SELECT password,private_key,Total_n FROM userKeys WHERE id=?",[toId])
	for data in query:
		pwd = data[0]
		privateKey = data[1]
		Total = data[2]

	connect.close()

	wind.title(sub)

	dec_privateKey = decrypt_this(privateKey, pwd)
	dec_sessionKey = rsaDecrypt(s_key, dec_privateKey, Total)
	encrypted_mail = decrypt_this(mail, str(dec_sessionKey))

	Label(wind,text=fromId).pack()
	Label(wind,text=toId).pack()
	Label(wind,text=sub).pack()
	Label(wind,text=encrypted_mail).pack()

	wind.mainloop()

# def outbox_mail_tk(mail_id):
# 	wind = Tk()
# 	wind.minsize(300,400)

# 	connect = sqlite3.connect("encmailtest.db")
# 	result = connect.execute("SELECT from_id,to_id,sub,mail,session_key from mail where id=?",[mail_id])
# 	for data in result:
# 		fromId = data[0]
# 		toId = data[1]
# 		sub = data[2]
# 		mail = data[3]
# 		s_key = data[4]

# 	query = connect.execute("SELECT public_key,Total_n FROM userKeys WHERE id=?",[fromId])
# 	for data in query:
# 		publicKey = data[0]
# 		Total = data[1]

# 	connect.close()

# 	#dec_privateKey = decrypt_this(privateKey, pwd)
# 	dec_sessionKey = rsaDecrypt(s_key, publicKey, Total)
# 	encrypted_mail = decrypt_this(mail, str(dec_sessionKey))

# 	Label(wind,text=fromId).pack()
# 	Label(wind,text=toId).pack()
# 	Label(wind,text=sub).pack()
# 	Label(wind,text=encrypted_mail).pack()

# 	wind.mainloop()

def rsaDecrypt(s_key, dec_privateKey, Total):
	length = len(s_key)
	x=1
	last=""
	a=[]
	for i in range (1, length-1):
		if s_key[i]==",":
			num = int(s_key[x:i])
			a=a+[num]
			x=i+2
	for i in range (x, length-1):
		last = last+s_key[i]
	a=a+[int(last)]
	sess_key = a
	privateKey = int(dec_privateKey)
	plain = [chr((char ** privateKey) % Total) for char in sess_key]
	x="".join(plain)
	return x

if __name__ == "__main__":
	inbox_mail_tk(11)