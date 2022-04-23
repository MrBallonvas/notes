import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql

con = sql.connect('note.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS note 
	(id INTEGER PRIMARY KEY, title_note TEXT, text_note TEXT)""")
print('done')

columns = ['#1', '#2', '#3']

def deleteSelectedNote(val):
	pass

def showNoteWin(val):
	showNoteWindow = tk.Tk()
	showNoteWindow.title('Full note window')
	showNoteWindow.geometry('500x500')

	lblTitle = tk.Label(showNoteWindow, text='Title:', bg='black', fg='white').pack()
	title = tk.Label(showNoteWindow, text='\n'+val[1]+'\n')
	title.pack()

	lblText = tk.Label(showNoteWindow, text='Text:', bg='black', fg='white').pack()
	text = tk.Label(showNoteWindow, text='\n'+val[2]+'\n')
	text.pack()

def openFullNote(event):
	global val

	item = treeview.selection()[0]

	val = treeview.item(item, option='values')

	print(str(val[0]))
	print(str(val[1]))
	print(str(val[2]))

	showNoteWin(val)

def updateTreeview():
	[treeview.delete(i) for i in treeview.get_children()]
	loadAllNotes()

def deleteAllNoteFunc():
	cur.execute("DELETE FROM note")
	con.commit()
	updateTreeview()

def loadAllNotes():
	cur.execute("SELECT * FROM note")
	res = cur.fetchall()

	print(res)
	print(len(res))

	for i in res:
		print('№: '+str(i[0]))
		print('title: '+str(i[1]))
		print('text: '+str(i[2]))
		treeview.insert('', index='end', values=(i[0], i[1], i[2]))

	con.commit()

def addNewNote(num, name, text):
	treeview.insert('', index='end', values=(num, name, text))

def pushTextData():
	getEntry = entry.get()
	getText = text.get(0.0, tk.END)
	print('Get entry: '+getEntry+'\n'+'Get text: '+getText)

	data = [str(getEntry), str(getText)]

	cur.execute("INSERT INTO note (title_note, text_note) VALUES (?,?)", data)

	con.commit()

	cur.execute('SELECT MAX(`id`) FROM note')
	a = cur.fetchall()

	print(str(a[0][0]))

	addNewNote(str(a[0][0]), getEntry, getText)

	createNewNote_Window.destroy()

def createNewNote_Win():
	global createNewNote_Window
	global entry
	global text

	createNewNote_Window = tk.Tk()
	createNewNote_Window.title('Create new note')
	createNewNote_Window.geometry('600x500')

	lblEntry = tk.Label(createNewNote_Window, text='Pls input note name').pack()
	entry = tk.Entry(createNewNote_Window)
	entry.pack()
	lblEntry = tk.Label(createNewNote_Window, text='Pls input text note').pack()
	text = tk.Text(createNewNote_Window)
	text.pack()
	createNewNote_Btn = tk.Button(createNewNote_Window, text='create', command=pushTextData)
	createNewNote_Btn.pack()

def main_win():
	global treeview
	global root

	root = tk.Tk()
	root.title('Notes')
	root.geometry('600x400')

	newNoteBtn = tk.Button(root, text='Create new note', command=createNewNote_Win)
	newNoteBtn.pack()
	deleteAllNoteBtn = tk.Button(root, text='Delete all notes', command=deleteAllNoteFunc)
	deleteAllNoteBtn.pack()

	treeview = ttk.Treeview(root, show='headings', columns=columns)

	treeview.heading('#1', text='№')
	treeview.heading('#2', text='Title')
	treeview.heading('#3', text='Text')

	scrl = ttk.Scrollbar(root, orient=tk.VERTICAL, command=treeview.yview)
	treeview.configure(yscroll=scrl.set)
	treeview.pack(side=tk.LEFT)

	treeview.bind("<Double-1>", openFullNote)

	loadAllNotes()

	root.mainloop()

def main():
	main_win()

if __name__ ==  '__main__':
	main()