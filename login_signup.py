import sqlite3
import random
import os
import sys
import unicodedata
from start import *
from inbox_frame import *
from Crypto.Util import number


class login_signup:
    def __init__(self):
        print ("checked login_signup.py \n")

    def login(self, email, password):
        print ("login checked")
        connection = sqlite3.connect("encmailtest.db")
        result = connection.execute("SELECT * FROM userKeys WHERE email=? AND password=?", (email, password))
        if (len(result.fetchall()) > 0):
            print ("user exist" )
            i_f = inbox_frame(email)
        else:
            print ("user doesn't exist")
            os.system('python3 start.py')
        connection.close()

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def multiplicative_inverse(self, e, phi):
        d = 0

        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi

        while e > 0:
            temp1 = temp_phi // e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2

            x = x2 - temp1 * x1
            y = d - temp1 * y1

            x2 = x1
            x1 = x
            d = y1
            y1 = y

        if temp_phi == 1:
            return d + phi

    def generate_keypair(self, p, q):
        n = p * q

        phi = (p - 1) * (q - 1)
        e = random.randrange(1, phi)
        g = self.gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)

        d = self.multiplicative_inverse(e, phi)
        return ((e, n), (d, n))

    def encryptPrivateKey(self, private, pwd):
        print("Private Key is", private)

        print("Password is", pwd)
        new_text = ""
        text = str(private)
        print ("the encrypted text is ",text)
        key = str(pwd)
        length = len(text)
        keyLength = len(key)
        for i in range(0, length):
            m = i % keyLength
            a = text[i]
            b = key[m]
            c = chr(ord(a) + ord(b))
            new_text = new_text + c
        private = new_text
        return private

    def signup(self, email, password):
        print ("signup clicked")
        name="dummy"

        a = email.find('@')
        b = email.find('.')
        print (a)
        print (b)
        if(a>0 and b>0):
            print("good")
            n = 8
            p = number.getPrime(n)
            q = number.getPrime(n)
            if p == q:
                p = number.getPrime(n)
            public, private = self.generate_keypair(p,q)
            print (public)
            print (private)
            public_key , n = public
            private_key, n = private
            private_key = encrypt_this(str(private_key), password)
            print ("Public Key is", public_key,"and total",n)
            print ("Private Key is",private_key)
            print ("Your public key is",public,"and private key is",private)

            private = self.encryptPrivateKey(private_key, password)
            connection = sqlite3.connect("encmailtest.db")
            connection.execute("INSERT INTO userKeys(name, email, password,public_key,private_key,Total_n) VALUES(?,?,?,?,?,?)",(name,email,password,public_key,private_key,n))
            connection.commit()
            connection.close()
            print ("authentication complete")
            os.system('python3 start.py')
        else:
        	print ("invalid mail")
        	os.system('python3 start.py')
