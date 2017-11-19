from interpreter import *
from calc import *
from gui import *

class Controller:

	def __init__(self):
		self.root = Tk()
		self.calc = Calc()
		self.interpreter = Interpreter(self.calc)

	def run(self):
		self.editor = IDE(self.root, self.interpreter)
		self.root.mainloop()
		

if __name__ == '__main__':
    c = Controller()
    c.run()		