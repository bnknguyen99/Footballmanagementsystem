#Import
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Style, Treeview
import mysql.connector as mc
import threading
from datetime import datetime
############
username= input('Please input your SQL username: ')
password= input('Please input your SQL password: ')
config = {
	'host':"localhost",
	'port': 3306,
	'user':username,
	'passwd':password,
	'database':"hanoifc",
	'charset': 'utf8',
	'use_unicode': True
}
#Connect to my SQL
mydb = mc.connect(**config)

#FUNCTION
def show_table(a):
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM %s"%a)
	myresult = mycursor.fetchall()
	pr=[]
	for i in range(len(myresult)):
		a=str(myresult[i])
		pr.append(a+'\n')
	return pr

def close():
	print('Thank you for using me!!!')
	sys.exit()

def split_p(pr2):	
	i=pr2.split(', ')
	yy='/'
	i[0]=i[0][1:]
	for stt in range(1,4):
		i[stt]=i[stt][1:-1]
	i[7]=i[7][:-3]
	if len(i[7])==1:
		i[7]='0'+i[7]
	if len(i[6])==1:
		i[6]='0'+i[6]
	i[5]=i[5][14:]+yy+i[6]+yy+i[7]

	i.pop()
	i.pop()
	return i

def split_c(pr2):
	i=pr2.split(', ')
	i[0]=i[0][1:-1]
	i[0]=i[0][1:]
	i[3]=i[3][1:-3]
	return i

def split_a(pr2):
	i=pr2.split(', ')
	i[0]=i[0][2:-1]
	i[1]=i[1][:-2]
	return i

def treview_init():
	global frame2
	global mainTable
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	pr2=show_table('player')
	print(pr2)
	haha=[]
	for i in pr2:
		haha.append(split_p(i))
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Num', 'Name', 'Nation', 'Position', 'Salary','Join day'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('Num', anchor='w', width=35)
	mainTable.heading('Num', text='Num')
	mainTable.column('Name', anchor='w', width=210)
	mainTable.heading('Name', text='Name')
	mainTable.column('Nation', anchor='w', width=120)
	mainTable.heading('Nation', text='Nation')
	mainTable.column('Position', anchor='w', width=120)
	mainTable.heading('Position', text='Position')
	mainTable.column('Salary', anchor='w', width=120)
	mainTable.heading('Salary', text='Salary(VNĐ/Month)')
	mainTable.column('Join day', anchor='center', width=120)
	mainTable.heading('Join day', text='Contract(y/m/d)')
	mainTable.pack()
	for i in range(len(pr2)):
		mainTable.insert('', 'end',values=(haha[i][0],'      '+haha[i][1],'      '+haha[i][2],'      '+haha[i][3],'          '+haha[i][4][1:-1],haha[i][5]))

def mlabel_player():
	global frame2
	global mainTable
	searchbutton.config(command= lambda: threading_s(search_player))
	button6.config(command=lambda: threading_s(update_player), state='active')
	button5.config(text='New player',command=lambda: threading_s(insert_player), state='active')
	button7.config(text='Sell him!!!', command=lambda: threading_s(delete_player), state='active')
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	pr2=show_table('player')
	haha=[]
	for i in pr2:
		haha.append(split_p(i))
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Num', 'Name', 'Nation', 'Position', 'Salary','Join day'),height='16', yscrollcommand = scrollbar.set)
	mainTable.tag_configure('odd', background='black')
	mainTable.tag_configure('even', background='#DFDFDF')
	mainTable['show'] = 'headings'
	mainTable.column('Num', anchor='w', width=35)
	mainTable.heading('Num', text='Num')
	mainTable.column('Name', anchor='w', width=210)
	mainTable.heading('Name', text='Name')
	mainTable.column('Nation', anchor='w', width=120)
	mainTable.heading('Nation', text='Nation')
	mainTable.column('Position', anchor='w', width=120)
	mainTable.heading('Position', text='Position')
	mainTable.column('Salary', anchor='w', width=120)
	mainTable.heading('Salary', text='Salary(VNĐ/Month)')
	mainTable.column('Join day', anchor='center', width=120)
	mainTable.heading('Join day', text='Contract(y/m/d)')
	mainTable.pack()
	for i in range(len(pr2)):
		mainTable.insert('', 'end',values=(haha[i][0],'      '+haha[i][1],'      '+haha[i][2],'      '+haha[i][3],'          '+haha[i][4][1:-1],haha[i][5]))
	return mainTable

def mlabel_coach():
	global frame2
	global mainTable
	searchbutton.config(command= lambda: threading_s(search_coach) )
	button6.config(command=lambda: threading_s(update_coach), state='active')
	button5.config(text='New staff',command=lambda: threading_s(insert_coach), state='active')
	button7.config(text='Fire Him!!!', command=lambda: threading_s(delete_coach), state='active')
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	pr2=show_table('coaching_staff')
	haha=[]
	for i in pr2:
					haha.append(split_p(i))
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('ID', 'Name', 'Nation', 'Position', 'Salary','Join day'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('ID', anchor='w', width=35)
	mainTable.heading('ID', text='ID')
	mainTable.column('Name', anchor='w', width=210)
	mainTable.heading('Name', text='Name')
	mainTable.column('Nation', anchor='w', width=120)
	mainTable.heading('Nation', text='Nation')
	mainTable.column('Position', anchor='w', width=125)
	mainTable.heading('Position', text='Position')
	mainTable.column('Salary', anchor='w', width=115)
	mainTable.heading('Salary', text='Salary(VNĐ/Month)')
	mainTable.column('Join day', anchor='center', width=120)
	mainTable.heading('Join day', text='Contract(y/m/d)')
	mainTable.pack()
	for i in range(len(pr2)):
		mainTable.insert('', 'end',values=(haha[i][0][1:-1],'      '+haha[i][1],'      '+haha[i][2],'      '+haha[i][3],'          '+haha[i][4][1:-1],haha[i][5]))
	return mainTable

def mlabel_sponsor():
	global frame2
	global mainTable
	searchbutton.config(command= lambda: threading_s(search_sponsor))
	button6.config(command=lambda: threading_s(update_sponsor), state='active')
	button5.config(text='New sponsor',command=lambda: threading_s(insert_sponsor), state='active')
	button7.config(text='Delete!!!', command=lambda: threading_s(delete_sponsor), state='active')
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	pr2=show_table('sponsor')
	haha=[]
	for i in pr2:
		haha.append(split_c(i))
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Name', 'Values', 'Duration', 'Note'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('Name', anchor='w', width=240)
	mainTable.heading('Name', text='Sponsorer')
	mainTable.column('Values', anchor='w', width=150)
	mainTable.heading('Values', text='Values(VNĐ)')
	mainTable.column('Duration', anchor='w', width=150)
	mainTable.heading('Duration', text='Duration')
	mainTable.column('Note', anchor='w', width=184)
	mainTable.heading('Note', text='Note')
	mainTable.pack()
	for i in range(len(pr2)):
		mainTable.insert('', 'end',values=('      '+haha[i][0],'      '+haha[i][1][1:-1],'           '+haha[i][2]+' Year(s)','      '+haha[i][3]))
	return mainTable

def mlabel_log():
	global frame2
	global mainTable
	searchbutton.config(command= lambda: threading_s(search_log))
	button6.config(state='disable')
	button5.config(state='disable')
	button7.config(state='disable')
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	pr2=show_table('activity_log')
	haha=[]
	for i in pr2:
		haha.append(split_a(i))
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Activity','ss'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('Activity', anchor='w',width=350)
	mainTable.heading('Activity', text='Activity')
	mainTable.column('ss', anchor='center',width=350)
	mainTable.heading('ss', text='Date(y/m/d)')
	mainTable.pack()
	def reversed(x):
		if hasattr(x, 'keys'):
			raise ValueError("mappings do not support reverse iteration")
		i = len(x)
		while i > 0:
			i -= 1
			yield x[i]
	for i in reversed(haha):
		mainTable.insert('', 'end',values=('                '+i[0],i[1][1:-1]))
	return mainTable

def delete_player():
	selected_item = mainTable.selection() ## get selected item
	for value in selected_item:
		s_item=mainTable.item(value,'values')[0]
		sss=mainTable.item(value,'values')[1]	
	mycursor=mydb.cursor()
	sql = "DELETE FROM player WHERE kit_number = "+(s_item)
	mycursor.execute(sql)
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Delete player:"+sss[6:]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()	
	mlabel_player()
	print(sss[6:], "was sold")

def delete_coach():
	selected_item = mainTable.selection() ## get selected item
	for value in selected_item:
		s_item=mainTable.item(value,'values')[0]
		sss=mainTable.item(value,'values')[1]
	mycursor=mydb.cursor()
	mycursor = mydb.cursor()
	sql = "DELETE FROM coaching_staff WHERE staff_id =\'"+s_item+"\'"
	mycursor.execute(sql)
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Delete staff:"+sss[6:]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()	
	mlabel_coach()
	print(sss[6:], "was fired")

def delete_sponsor():
	selected_item = mainTable.selection() ## get selected item
	for value in selected_item:
		s_item=mainTable.item(value,'values')[0]
		sss=mainTable.item(value,'values')[0]
	mycursor=mydb.cursor()
	mycursor = mydb.cursor()
	sql = "DELETE FROM sponsor WHERE sponsor_name =\'"+s_item[6:]+"\'"
	mycursor.execute(sql)
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Delete sponsor:"+sss[6:]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()	
	mlabel_sponsor()
	print(sss[6:], "was deleted")

def insert_player():
	mycursor = mydb.cursor()
	sql = "insert into player (kit_number, player_name, nationality, player_position, salary, new_signed_contract ) VALUES (%s, %s, %s, %s, %s, %s)"
	ss=new_entry(['Kit Number :','Name :','Nation :','Position :','Salary :', 'Contract :'])
	val = (po[0],po[1],po[2],po[3],po[4],po[5])
	mycursor.execute(sql, val)
	s=mycursor.rowcount
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Insert player:"+po[1]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()
	print(s, "record inserted.")
	mlabel_player()

def insert_coach():
	mycursor = mydb.cursor()
	sql = "insert into coaching_staff (staff_id, staff_name, nationality, staff_position, salary, new_signed_contract ) VALUES (%s, %s, %s, %s, %s, %s)"
	ss=new_entry(['ID :','Name :','Nation :','Position :','Salary :', 'Contract :'])
	val = (po[0],po[1],po[2],po[3],po[4],po[5])
	mycursor.execute(sql, val)
	s=mycursor.rowcount
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Insert staff:"+po[1]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()
	print(s, "record inserted.")
	mlabel_coach()

def insert_sponsor():
	mycursor = mydb.cursor()
	sql = "insert into sponsor(sponsor_name, contract_value, duration, note) values (%s, %s, %s, %s)"
	ss=new_entry_s()
	val = (po[0],po[1],po[2],po[3])
	mycursor.execute(sql, val)
	s=mycursor.rowcount
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Insert sponsor:"+po[0]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()
	print(s, "record inserted.")
	mlabel_sponsor()

def update_player():
	selected_item = mainTable.selection() ## get selected item
	for value in selected_item:
		s_item=mainTable.item(value,'values')
	s_items=list(s_item)	
	s_items[1]=s_items[1][6:]
	s_items[2]=s_items[2][6:]
	s_items[3]=s_items[3][6:]
	s_items[4]=s_items[4][10:]
	new_entryupdate(['Kit Number :','Name :','Nation :','Position :','Salary :', 'Contract :'] ,s_items)
	val=list(po)
	sql = "Replace into player (kit_number, player_name, nationality, player_position, salary, new_signed_contract) values (%s, %s, %s, %s, %s, %s)"
	mycursor = mydb.cursor()
	mycursor.execute(sql,val)
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Update player:"+po[1]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	print(po[1],'was updated')
	mydb.commit()
	mlabel_player()

def update_coach():
	selected_item = mainTable.selection() ## get selected item
	for value in selected_item:
		s_item=mainTable.item(value,'values')
	s_items=list(s_item)	
	s_items[1]=s_items[1][6:]
	s_items[2]=s_items[2][6:]
	s_items[3]=s_items[3][6:]
	s_items[4]=s_items[4][10:]
	new_entryupdate(['id :','Name :','Nation :','Position :','Salary :', 'Contract :'] ,s_items)
	val=list(po)
	sql = "Replace into coaching_staff (staff_id, staff_name, nationality, staff_position, salary, new_signed_contract) values (%s, %s, %s, %s, %s, %s)"
	mycursor = mydb.cursor()
	mycursor.execute(sql,val)
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Update staff:"+po[1]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	print(po[1],'was updated')
	mydb.commit()
	mlabel_coach()

def update_sponsor():
	selected_item = mainTable.selection() ## get selected item
	for value in selected_item:
		s_item=mainTable.item(value,'values')
	s_items=list(s_item)
	s_items[0]=s_item[0][6:]
	s_items[1]=s_item[1][6:]
	s_items[2]=s_item[2][11:-8]
	s_items[3]=s_item[3][6:]
	new_entry_supdate(s_items)
	mycursor = mydb.cursor()
	sql = "Replace into sponsor(sponsor_name, contract_value, duration, note) values (%s, %s, %s, %s)"
	val = (po[0],po[1],po[2],po[3])
	mycursor.execute(sql, val)
	s=mycursor.rowcount
	d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	log="insert into activity_log (activity, etad) VALUES (\'Update sponsor:"+po[0]+"\', \'"+d1+"\')"
	mycursor.execute(log)
	mydb.commit()
	print(s, "record inserted.")
	mlabel_sponsor()

def new_entry(a):
	def get():
		global po
		po=[E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get()]
		top.destroy()
	top = Tk()
	top.geometry('277x300')
	L1 = Label(top, text=a[0])
	L1.place(x=10, y=10)
	L2 = Label(top, text=a[1])
	L2.place(x=10, y=50)
	L3 = Label(top, text=a[2])
	L3.place(x=10, y=90)
	L4 = Label(top, text=a[3])
	L4.place(x=10, y=130)
	L5 = Label(top, text=a[4])
	L5.place(x=10, y=170)
	L6 = Label(top, text=a[5][:-1]+'(y/m/d):')
	L6.place(x=10, y=210)
	E1 = Entry(top, bd =5)
	E1.place(x=115, y=10)
	E2 = Entry(top, bd =5)
	E2.place(x=115, y=50)
	E3 = Entry(top, bd =5)
	E3.place(x=115, y=90)
	E4 = Entry(top, bd =5)
	E4.place(x=115, y=130)
	E5 = Entry(top, bd =5)
	E5.place(x=115, y=170)
	E6 = Entry(top, bd =5)
	E6.place(x=115, y=210)
	but=Button(top, text='OK', height=2, width=6, font='Arial 10 bold', bg='#b3b3b3',command=get)
	but.place(x=210, y=250)
	top.mainloop()

def new_entry_s():
	def get():
		global po
		po=[E1.get(),E2.get(),E3.get(),E4.get()]
		top.destroy()
	top = Tk()
	top.geometry('277x300')
	L1 = Label(top, text='Sponsorer')
	L1.place(x=10, y=10)
	L2 = Label(top, text='Value(VNĐ)')
	L2.place(x=10, y=50)
	L3 = Label(top, text='Duration(Year)')
	L3.place(x=10, y=90)
	L4 = Label(top, text='Note')
	L4.place(x=10, y=130)
	E1 = Entry(top, bd =5)
	E1.place(x=115, y=10)
	E2 = Entry(top, bd =5)
	E2.place(x=115, y=50)
	E3 = Entry(top, bd =5)
	E3.place(x=115, y=90)
	E4 = Entry(top, bd =5)
	E4.place(x=115, y=130)
	but=Button(top, text='OK', height=2, width=6, font='Arial 10 bold', bg='#b3b3b3',command=get)
	but.place(x=210, y=250)
	top.mainloop()

def new_entryupdate(a,b):
	def get():
		global po
		po=[E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get()]
		top.destroy()
	top = Tk()
	top.geometry('277x300')
	L1 = Label(top, text=a[0])
	L1.place(x=10, y=10)
	L2 = Label(top, text=a[1])
	L2.place(x=10, y=50)
	L3 = Label(top, text=a[2])
	L3.place(x=10, y=90)
	L4 = Label(top, text=a[3])
	L4.place(x=10, y=130)
	L5 = Label(top, text=a[4])
	L5.place(x=10, y=170)
	L6 = Label(top, text=a[5][:-1]+'(y/m/d):')
	L6.place(x=10, y=210)
	E1 = Entry(top, bd =5)
	E1.place(x=115, y=10)
	E1.insert(0,b[0])
	E1.config(state='disable')
	E2 = Entry(top, bd =5)
	E2.place(x=115, y=50)
	E2.insert(0,b[1])
	E3 = Entry(top, bd =5)
	E3.place(x=115, y=90)
	E3.insert(0,b[2])
	E4 = Entry(top, bd =5)
	E4.place(x=115, y=130)
	E4.insert(0,b[3])
	E5 = Entry(top, bd =5)
	E5.place(x=115, y=170)
	E5.insert(0,b[4])
	E6 = Entry(top, bd =5)
	E6.place(x=115, y=210)
	E6.insert(0,b[5])
	but=Button(top, text='OK', height=2, width=6, font='Arial 10 bold', bg='#b3b3b3',command=get)
	but.place(x=210, y=250)
	top.mainloop()

def new_entry_supdate(a):
	def get():
		global po
		po=[E1.get(),E2.get(),E3.get(),E4.get()]
		top.destroy()
	top = Tk()
	top.geometry('277x300')
	L1 = Label(top, text='Sponsorer')
	L1.place(x=10, y=10)
	L2 = Label(top, text='Value(VNĐ)')
	L2.place(x=10, y=50)
	L3 = Label(top, text='Duration(Year)')
	L3.place(x=10, y=90)
	L4 = Label(top, text='Note')
	L4.place(x=10, y=130)
	E1 = Entry(top, bd =5)
	E1.place(x=115, y=10)
	E1.insert(0,a[0])
	E1.config(state='disable')
	E2 = Entry(top, bd =5)
	E2.place(x=115, y=50)
	E2.insert(0,a[1])
	E3 = Entry(top, bd =5)
	E3.place(x=115, y=90)
	E3.insert(0,a[2])
	E4 = Entry(top, bd =5)
	E4.place(x=115, y=130)
	E4.insert(0,a[3])
	but=Button(top, text='OK', height=2, width=6, font='Arial 10 bold', bg='#b3b3b3',command=get)
	but.place(x=210, y=250)
	top.mainloop()

def time():
	timelabel.config(text= datetime.now().strftime("%d/%m/%Y %H:%M:%S"), bg="#003333")
	timelabel.after(1000, time)

def threading_s(s):
	thread1 = threading.Thread(target=s)
	thread1.start()

def menu_bar():
	menubar = Menu(window)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="New player", command=lambda: threading_s(insert_player))
	filemenu.add_command(label="Delete player", command=lambda: threading_s(delete_player))
	filemenu.add_command(label="New staff", command=lambda: threading_s(insert_coach))
	filemenu.add_command(label="Delete staff", command=lambda: threading_s(delete_coach))
	filemenu.add_command(label="New sponsorer",command=lambda: threading_s(insert_sponsor))
	filemenu.add_command(label="Delete sponsorer", command=lambda: threading_s(delete_sponsor))
	filemenu.add_command(label="Save")
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=close)
	menubar.add_cascade(label="Tasks", menu=filemenu)
	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label="About...")
	menubar.add_cascade(label="Help",menu=helpmenu)
	window.config(menu=menubar)

def search_player():
	s=entry1.get().lower()
	pr2=show_table('player')
	haha=[]
	ssss=[]
	for i in pr2:
		haha.append(split_p(i))
	for item in haha:
		if s in item[0].lower() or s in item[1].lower() or s in item[2].lower() or s in item[3].lower() or s in item[4].lower() or s in item[5].lower():
			ssss.append(item)
	global frame2
	global mainTable
	button6.config(command=lambda: threading_s(update_player))
	button5.config(text='New player',command=lambda: threading_s(insert_player))
	button7.config(text='Sell him!!!', command=lambda: threading_s(delete_player))
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Num', 'Name', 'Nation', 'Position', 'Salary','Join day'),height='16', yscrollcommand = scrollbar.set)
	mainTable.tag_configure('odd', background='black')
	mainTable.tag_configure('even', background='#DFDFDF')
	mainTable['show'] = 'headings'
	mainTable.column('Num', anchor='w', width=35)
	mainTable.heading('Num', text='Num')
	mainTable.column('Name', anchor='w', width=210)
	mainTable.heading('Name', text='Name')
	mainTable.column('Nation', anchor='w', width=120)
	mainTable.heading('Nation', text='Nation')
	mainTable.column('Position', anchor='w', width=120)
	mainTable.heading('Position', text='Position')
	mainTable.column('Salary', anchor='w', width=120)
	mainTable.heading('Salary', text='Salary(GBP/week)')
	mainTable.column('Join day', anchor='center', width=120)
	mainTable.heading('Join day', text='Contract(y/m/d)')
	mainTable.pack()
	for i in range(len(ssss)):
		mainTable.insert('', 'end',values=(ssss[i][0],'      '+ssss[i][1],'      '+ssss[i][2],'      '+ssss[i][3],'          '+ssss[i][4], ssss[i][5]))
	return mainTable

def search_coach():
	s=entry1.get().lower()
	pr2=show_table('coaching_staff')
	haha=[]
	ssss=[]
	for i in pr2:
		haha.append(split_p(i))
	for item in haha:
		if s in item[0].lower() or s in item[1].lower() or s in item[2].lower() or s in item[3].lower() or s in item[4].lower() or s in item[5].lower():
			ssss.append(item)
	global frame2
	global mainTable
	button6.config(command=lambda: threading_s(update_coach))
	button5.config(text='New Staff',command=lambda: threading_s(insert_coach))
	button7.config(text='Fire him!!!', command=lambda: threading_s(delete_coach))
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('ID', 'Name', 'Nation', 'Position', 'Salary','Join day'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('ID', anchor='w', width=35)
	mainTable.heading('ID', text='ID')
	mainTable.column('Name', anchor='w', width=210)
	mainTable.heading('Name', text='Name')
	mainTable.column('Nation', anchor='w', width=120)
	mainTable.heading('Nation', text='Nation')
	mainTable.column('Position', anchor='w', width=125)
	mainTable.heading('Position', text='Position')
	mainTable.column('Salary', anchor='w', width=115)
	mainTable.heading('Salary', text='Salary(GBP/week)')
	mainTable.column('Join day', anchor='center', width=120)
	mainTable.heading('Join day', text='Contract(y/m/d)')
	mainTable.pack()
	for i in range(len(ssss)):
		mainTable.insert('', 'end',values=(ssss[i][0][1:-1],'      '+ssss[i][1],'      '+ssss[i][2],'      '+ssss[i][3],'          '+ssss[i][4],ssss[i][5]))
	return mainTable

def search_sponsor():
	s=entry1.get().lower()
	pr2=show_table('sponsor')
	haha=[]
	ssss=[]
	for i in pr2:
		haha.append(split_c(i))
	for item in haha:
		if s in item[0].lower() or s in item[1].lower() or s in item[2].lower() or s in item[3].lower():
			ssss.append(item)
	global frame2
	global mainTable
	button6.config(command=lambda: threading_s(update_sponsor))
	button5.config(text='New sponsor',command=lambda: threading_s(insert_sponsor))
	button7.config(text='Delete!!!', command=lambda: threading_s(delete_sponsor))
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	pr2=show_table('sponsor')
	haha=[]
	for i in pr2:
		haha.append(split_c(i))
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Name', 'Values', 'Duration', 'Note'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('Name', anchor='w', width=240)
	mainTable.heading('Name', text='Sponsorer')
	mainTable.column('Values', anchor='w', width=150)
	mainTable.heading('Values', text='Values(VNĐ)')
	mainTable.column('Duration', anchor='w', width=150)
	mainTable.heading('Duration', text='Duration')
	mainTable.column('Note', anchor='w', width=184)
	mainTable.heading('Note', text='Note')
	mainTable.pack()
	for i in range(len(ssss)):
		mainTable.insert('', 'end',values=('      '+ssss[i][0],'      '+ssss[i][1][1:-1],'           '+ssss[i][2]+' Year(s)','      '+ssss[i][3]))
	return mainTable

def search_log():
	s=entry1.get().lower()
	pr2=show_table('activity_log')
	haha=[]
	ssss=[]
	for i in pr2:
		haha.append(split_a(i))
	for item in haha:
		if s in item[0].lower() or s in item[1].lower():
			ssss.append(item)
	global frame2
	global mainTable
	frame2.destroy()
	frame2=Frame(frame1, relief=RIDGE)
	frame2.pack(side = LEFT,pady=5,padx=18)
	scrollbar = Scrollbar(frame2)
	scrollbar.pack( side = RIGHT, fill = Y )
	mainTable = ttk.Treeview(frame2, columns=('Activity','ss'),height='16', yscrollcommand = scrollbar.set)
	mainTable['show'] = 'headings'
	mainTable.column('Activity', anchor='w',width=350)
	mainTable.heading('Activity', text='Activity')
	mainTable.column('ss', anchor='center',width=350)
	mainTable.heading('ss', text='Date(y/m/d)')
	mainTable.pack()
	def reversed(x):
		if hasattr(x, 'keys'):
			raise ValueError("mappings do not support reverse iteration")
		i = len(x)
		while i > 0:
			i -= 1
			yield x[i]
	for i in reversed(ssss):
		mainTable.insert('', 'end',values=('                '+i[0],i[1][1:-1]))
	return mainTable
	
#WINDOW
window=Tk()
window.geometry('1020x475')
thrd=0
#UI
window.title("FMS")
window.style = ttk.Style()
window.style.theme_use("default")
frame1 = Frame(window, relief=RIDGE, borderwidth=1)
frame1.pack(fill=BOTH, expand=True)

lbl1=Label(frame1,text='HÀ NỘI FOOTBALL CLUB', fg='#00ffff'
														  , font='Arial 25 bold'
														  , bg= '#003333')
lbl1.pack(side=TOP, ipadx=289, pady=3, ipady=10,)
entry1 = Entry(frame1,width=75, fg='black', bg="white",font='Arial 13')
entry1.pack(anchor='nw',padx=19)
timelabel = Label(window,fg='#00ffff', font='Arial 10 bold')
timelabel.place(x=19, y=448)
time()
#Main Frame
treview_init()

#Button's Frame
frame3 = Frame(frame1, relief=RIDGE)
frame3.pack(side=RIGHT, padx=10)
button1 = Button(frame3, text='Player', bg='#b3b3b3', font='Arial 10 bold', command=mlabel_player,width=18)
button1.pack(padx=30, pady=9,)
button2 = Button(frame3, text='Staff', bg='#b3b3b3', font='Arial 10 bold', command=mlabel_coach, width=18)
button2.pack(padx=30, pady=10)
button3 = Button(frame3, text='Sponsor', bg='#b3b3b3', font='Arial 10 bold', width=18, command=mlabel_sponsor)
button3.pack(padx=30, pady=10)
button4 = Button(frame3, text='Activity log', bg='#b3b3b3', font='Arial 10 bold', width=18, command=mlabel_log)
button4.pack(padx=30, pady=10)
button5 = Button(frame3, text='New player', bg='#ffffff', font='Arial 10 bold', width=18, command=lambda: threading_s(insert_player))
button5.pack(padx=30, pady=10)
button6 = Button(frame3, text='Update',bg='#ffffff', font='Arial 10 bold', width=18, command=lambda: threading_s(update_player))
button6.pack(padx=30, pady=10)
button7 = Button(frame3, text='Sell Him!!', bg='#ffffff', font='Arial 10 bold', command=lambda: threading_s(delete_player), width=18)
button7.pack(padx=30, pady=10)
searchbutton = Button(frame1, text= 'Search', relief=FLAT, width=9, font='Arial 8', command=lambda: threading_s(search_player))
searchbutton.place(x=695, y=69)
closeButton = Button(window, text="Close", bg='#b3b3b3', command=close)
closeButton.pack(side=RIGHT, padx=5, pady=5, ipadx=50)


#MAINLOOP
menu_bar()
window.resizable(0,0)
window.mainloop()
