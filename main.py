import tkinter as tk
import sqlite3 as sql

con = sql.connect('note.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS note 
	(id INTEGER PRIMARY KEY, title_note TEXT, text_note TEXT)""")
print('done')

def deleteAllNoteFunc():
	cur.execute("DELETE FROM note")
	con.commit()

def pushTextData():
	getEntry = entry.get()
	getText = text.get(0.0, tk.END)
	print('Get entry: '+getEntry+'\n'+'Get text: '+getText)

	data = [str(getEntry), str(getText)]

	res = cur.fetchall()
	print(res)

	cur.execute("INSERT INTO note (title_note, text_note) VALUES (?,?)", data)

	res2 = cur.fetchall()
	print(res2)
	con.commit()
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
	root = tk.Tk()
	root.title('Notes')
	root.geometry('400x600')

	newNoteBtn = tk.Button(root, text='Create new note', command=createNewNote_Win)
	newNoteBtn.pack()
	deleteAllNoteBtn = tk.Button(root, text='Delete all notes', command=deleteAllNoteFunc)
	deleteAllNoteBtn.pack()

	root.mainloop()

def main():
	main_win()

if __name__ ==  '__main__':
	main()

