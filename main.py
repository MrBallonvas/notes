import tkinter as tk
import sqlite3 as sql

con = sql.connect('note.db')
cur = con.cursor()
print('done')

def main_win():
	root = tk.Tk()
	root.title('Notes')
	root.geometry(str(400)+'x'+str(600))

	Label = tk.Label(root, text='Our notes').pack()

	root.mainloop()

def main():
	pass

if __name__ ==  '__main__':
	main()

