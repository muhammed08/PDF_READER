import PyPDF2
from tkinter.filedialog import askopenfilename
from  tkinter import *
import tkinter
import tkinter.messagebox as messagebox
from gtts import gTTS
import os
import sys
import time
no=0
numpage=0
start=False
def showabout():
	messagebox.showinfo('ABOUT','Created By: Muhammed Ameen\nContact:muhammedameen08@gmail.com')
def start_page():
	global no
	num=e.get()
	try:
		
		no=int(num)
		no=no-1;
		if (root.filename==""):
			messagebox.showerror("File_Error","Please Enter a valid file")
		elif(no>numpage):
			messagebox.showerror("Page_Error","Please Enter a valid page number")
		else:
			global start
			start=True
			root.destroy()
		return
	except ValueError:
		messagebox.showerror("Type Error","Please enter a Valid Value")




def start_reading():
	check=1;
	while(check==1):
		root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
		print (root.filename)
		check=0
		"""if(root.filename==""):
			messagebox.showerror("File_Error","Please Enter a valid file")
		else:
			check=0"""
	fileSel.configure(text= root.filename)
	global reader
	reader = PyPDF2.PdfFileReader(root.filename)
	
	global numpage
	numpage=reader.numPages
	txt="Total No of Page: "+str(numpage)
	det=Label(root,text=txt,width=30,height=5)
	det.pack()
	"""
	print("please enter the page")
	no=input()
	page=int(no)
	"""
	
root=Tk()
root.title("PDF READER")
root.geometry("400x300")
fileSel=Label(root,text="NO FILE SELECTED",height=2)
fileSel.pack()
button1 = Button(root, text="SELECT PDF", width=25, command=start_reading ,height = 2,background='#ADD8E6')
button1.pack()
lab=Label(root,text='Select Page',width=30,height=4)
lab.pack()
content=IntVar()
e = Entry(root,textvariable=content,width=30)
e.delete(0, END)
e.pack()
button2 = Button(root, text='START', width=25, command=start_page,height=2,background='#ADD8E6')
button2.pack()
var1 = IntVar()
chk=Checkbutton(root, text="Open PDF while reading", variable=var1,width=25,height=2)
chk.pack()
button3 = Button(root, text='ABOUT', width=25, command=showabout,height=2,background='#ADD8E6')
button3.pack(side=BOTTOM)
#e.focus_set()
root.mainloop()
page=int(no)
#file=open(name,"wb")
if(start):
	import pyttsx3
	engine = pyttsx3.init()
	if(page > reader.numPages):
		messagebox.showerror("Non-Int Error","Please enter a int")
		selpage()
	else:
		pageno=reader.getPage(page)
		pagetext=pageno.extractText()
		tts = gTTS(text=pagetext, lang='en')
		tts.save("page.mp3")
		os.startfile("page.mp3")
		if(var1.get()):
			os.startfile(root.filename)
		#os.system("mpg321 good.mp3")
"""
		engine.setProperty('rate',50)  #120 words per minute
		engine.setProperty('volume',0.9) 
		engine.say(pagetext)
		engine.runAndWait()
"""