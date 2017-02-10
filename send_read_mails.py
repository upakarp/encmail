import sqlite3
import unicodedata 
from encrypt_decrypt import *
import random

def send(from_mail,to_mail,subject_email,mail):
	print ("send")
	connection = sqlite3.connect("encmailtest.db")
	result = connection.execute("SELECT id from userKeys WHERE email = ?",[from_mail])
	for data in result:
		from_id = data[0]
	result = connection.execute("SELECT id,public_key,Total_n from userKeys WHERE email = ?",[to_mail])
	for data in result:
		to_id=data[0]
		public_key=data[1]
		total_n=data[2]
	session_key = random.randrange(1,200)
	sess_key = str(session_key)
	print("Session key is",sess_key)
	enc_mail = encrypt_this(mail,sess_key)
	cipher = rsaEncrypt(session_key, public_key, total_n)
	c = str(cipher)
	#s_key = ''.join(map(lambda x: str(x),cipher))
	connection.execute("INSERT INTO mail(from_id, to_id, sub, mail,session_key) VALUES(?,?,?,?,?)",(from_id,to_id,subject_email,enc_mail,c))
	connection.commit()
	print ("Success sent")
	connection.close()


def rsaEncrypt(enc_msg, pub_key, total):
	msg = str(enc_msg)
	cipher = [(ord(char) ** pub_key) % total for char in msg]
	return cipher

def read_inbox(from_email,lb):
	print ("read inbox")
	connection = sqlite3.connect("encmailtest.db")
	result = connection.execute("SELECT id FROM userKeys where email=?",[from_email])
	for data in result:
		i=1
		dict_data=[]
		result2 = connection.execute("SELECT sub,id FROM mail where to_id=?",[data[0]])
		for data2 in result2:
			# str=unicodedata.normalize('NFKD', data2[0]).encode('ascii','ignore')
			dict_data=dict_data+[data2[1]]
			lb.insert(i,data2[0])
			i=i+1
	print (dict_data)
	return dict_data

# def read_outbox(from_email,lb):
# 	print ("read outbox")
# 	connection = sqlite3.connect("encmailtest.db")
# 	result = connection.execute("SELECT id FROM userKeys where email=?",[from_email])
# 	for data in result:
# 		i=1
# 		dict_data=[]
# 		result2 = connection.execute("SELECT sub,id FROM mail where from_id=?",[data[0]])
# 		for data2 in result2:
# 			# str=unicodedata.normalize('NFKD', data2[0]).encode('ascii','ignore')
# 			dict_data=dict_data+[data2[1]]
# 			lb.insert(i,data2[0])
# 			i=i+1
# 	return dict_data