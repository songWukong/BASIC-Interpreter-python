from Tkinter import *

class guiView:

	def __init__(self, window):

		self.window = window
		window.geometry("500x510")
		window.configure(background = '#dddddd')
		window.resizable(False, False)
		window.title("Basic interpreter")

		self.listFrame = Frame(window)
		listFrame = self.listFrame
		listFrame.pack()
		
		self.listNodes = Listbox(listFrame)
		listNodes = self.listNodes
		listNodes.configure(width = 47,
							height = 20,
							bg = "#343833",
							fg = "#00FF00",
							font = ("Courier", 12, "bold"),
							borderwidth = 6,
							selectbackground = "#707a6e",
							selectforeground = "#ffffff",
							relief="sunken")

		

		self.scrollbar = Scrollbar(listFrame)
		scrollbar = self.scrollbar
		scrollbar.config(orient = "vertical",
						 command = listNodes.yview)

		scrollbar.pack(side = "right", fill = "y")

		listNodes.config(yscrollcommand = scrollbar.set)
		listNodes.bind('<<ListboxSelect>>', self.selectLine)
		listNodes.pack(side = "left", fill = BOTH)

		self.text = Text(window, height = 1)
		text = self.text
		text.configure(bg = "#343833",
					   fg = "#00FF00",
					   insertbackground = "#00ff00",
					   font = ("Courier", 12, "bold"),
					   borderwidth = 6,
					   highlightthickness = 14,
					   highlightcolor = "#dddddd",
					   selectbackground = "#707a6e",
					   selectforeground = "#ffffff",
					   relief="sunken")

		text.bind('<Return>', self.endLine)
		text.focus_set()
		text.pack()

		window.call(text, 'configure', '-blockcursor', True)

		self.name = Label(root)
		name = self.name
		name.configure(width = 65,
					   bg = "#dddddd",
					   text = "BASIC Interpreter",
					   font = ("Courier", 12, "bold"))
		
		name.pack()

	def endLine(self, event):

		lineNum = END		
		text = self.text
		listNodes = self.listNodes

		if (text.get("1.0", 'end-1c')[:1] == "\n"):
			text.delete('1.0')

		if (len(self.listNodes.curselection()) > 0):
			lineNum = int(self.listNodes.curselection()[0])
		
		if (lineNum != END):
			listNodes.insert(lineNum, text.get("1.0", END))
			listNodes.delete(lineNum + 1)
			lineNum = END
			listNodes.selection_clear(0, END)

		else:	
			listNodes.insert(lineNum, text.get("1.0", END))
		
		listNodes.see(END)
		text.delete('1.0', END)

	def selectLine(self, event):

		w = event.widget	
		
		try:
			lineNum = int(w.curselection()[0])	
			activeLine = w.get(lineNum)	
		except (IndexError, UnboundLocalError):
			activeLine = self.text.get("1.0", END)


		text = self.text
		text.delete('1.0', END)
		text.insert('1.0', activeLine)
 
root = Tk()
main = guiView(root)
root.mainloop()		
