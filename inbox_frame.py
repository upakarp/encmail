from tkinter import Tk, Button, Entry, Frame, Label, Text, Scrollbar, Listbox
from send_read_mails import *
from readmail_tk import *

class inbox_frame:

	def __init__(self,email):

		this = Tk()
		this.minsize(800,600)
		this.title(email)

		a=email.split('@')
		label = Label(this,text=a[0]).pack(pady=(2,0))

		frame_compose=Frame(this)
		frame_compose_1=Frame(frame_compose)
		Label(frame_compose_1,text="     To : ",width=10).pack(side="left")
		compose_to = Entry(frame_compose_1, width=30)
		compose_to.pack(ipady="1")

		frame_compose_2=Frame(frame_compose)
		Label(frame_compose_2,text="Subject : ",width=10).pack(side="left")
		compose_subject = Entry(frame_compose_2, width=30)
		compose_subject.pack(ipady="1")

		frame_compose_3=Frame(frame_compose)
		Label(frame_compose_3,text="Mail",).pack()
		compose_mail = Text(frame_compose_3,width=80)
		compose_mail.pack()

		def compose_send_clicked():
			print ("compose send clicked")
			from_email = email
			to_email = compose_to.get()
			subject_email = compose_subject.get()
			mail = compose_mail.get("1.0",'end-1c')
			send(from_email,to_email,subject_email,mail)
		compose_send=Button(frame_compose, text="send", command=compose_send_clicked)

		frame_inbox=Frame(this)
		def on_inbox(evt):
			w = evt.widget
			index = int(w.curselection()[0])
			value = w.get(index)
			print (value)
			id_mail= inbox_dictionary[index]
			print (id_mail)
			inbox_mail_tk(id_mail)

		# frame_outbox=Frame(this)
		# def on_outbox(evt):
		# 	w = evt.widget
		# 	index = int(w.curselection()[0])
		# 	value = w.get(index)
		# 	id_mail = outbox_dictionary[index]
		# 	print (id_mail)
		# 	outbox_mail_tk(id_mail)

		inbox_lb = Listbox(frame_inbox,height=30,width=80)
		inbox_lb.bind('<<ListboxSelect>>', on_inbox)

		# outbox_lb = Listbox(frame_outbox,height=30,width=80)
		# outbox_lb.bind('<<ListboxSelect>>', on_outbox)

		def compose_clicked():
			frame_inbox.pack_forget()
			# frame_outbox.pack_forget()
			frame_compose.pack()
			frame_compose_1.pack(pady=(0,3))
			frame_compose_2.pack(pady=(0,3))
			frame_compose_3.pack(pady=(0,3))
			compose_send.pack()

		def inbox_clicked():
			i_s = inbox_lb.size()
			inbox_lb.delete(0, i_s)
			frame_compose.pack_forget()
			# frame_outbox.pack_forget()
			frame_inbox.pack()
			inbox_lb.pack()
			dic=read_inbox(email,inbox_lb)
			global inbox_dictionary
			inbox_dictionary = dic

		# def sent_clicked():
		# 	o_s = outbox_lb.size()
		# 	outbox_lb.delete(0, o_s)
		# 	frame_compose.pack_forget()
		# 	frame_inbox.pack_forget()
		# 	frame_outbox.pack()
		# 	outbox_lb.pack()
		# 	print ("sent clicked")
		# 	dic=read_outbox(email,outbox_lb)
		# 	global outbox_dictionary
		# 	outbox_dictionary = dic

		frama = Frame(this)
		frama.pack(pady=(10,10))

		compose = Button(frama,text="compose",command=compose_clicked, width=10)
		compose.pack(side ="left")
		inbox = Button(frama,text="inbox",command=inbox_clicked, width=10)
		inbox.pack(side="left")
		# sent = Button(frama,text="sent",command=sent_clicked, width=10)
		# sent.pack(side="left")

		this.mainloop()

if __name__ == '__main__':
	inbox_frame("swat@gmail.com")

