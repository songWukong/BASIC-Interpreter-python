from calc import *

class Interpreter:

	__variables = {}
	
	def __init__(self, calc):

		self.calc = calc	

	def run(self):
		source = open("source.bas", "r").read()
		self.__tokenize_Program__(source)

	def __tokenize_Program__(self, source):

		code = list(source)
		self.__tokenize_Line__(code)


	def __tokenize_Line__(self, code):
		
		if (code[0] != "\n"):
			self.__tokenize_Symbol__(code)

		try:
			while (code[0] == "\n"):
				del code[0]
				self.__tokenize_Symbol__(code)		

		except (IndexError):		
			pass

	def __tokenize_Statement__(self, code):

		tokLen = len(code)
		token = ""
		i = 0
		
		while (code[0].isupper() == True):

			token += code[0]
			del code[0]

			i += 1

		if (token == "PRINT"):
			del code[0]
			self.__parse_Print__(code)

		elif (token == "LET"):
			del code[0]
			self.__parse_Let__(code)	 	

		return 1	


	def __tokenize_Symbol__(self, code):

		if (code[0] == " "):
			del code[0]

		elif (code[0].isupper):
			self.__tokenize_Statement__(code)


	def __parse_String__(self, code):
		
		string = ""
		i = 0

		while (code[0] != '\"'):
		
			string += code[0]
			del code[0]
			i += 1
		
		return string;
		

	def __parse_Print__(self, code):

		if (code[0] == "\""):
			del code[0]
			print self.__parse_String__(code)
			del code[0]

		elif (code[0].isdigit()):
			num = self.calc.parse_Formula(code)
			print num


	def __parse_Let__(self, code):
	
		varName = ""
		varVal = ""

		while (code[0] != "="):
			varName += code[0]
			del code[0]

		if (code[0] == "="):
			del code[0]

			try:
				while (code[0] != "\n"):

					if (code[0].isdigit()):
						varVal += code[0]
						del code[0]

			except (IndexError):
				self.__variables[varName] = int(varVal)	
				print self.__variables
				return									
			
		self.__variables[varName] = int(varVal)
		print self.__variables	


calc = Calc()
interpreter = Interpreter(calc)
interpreter.run()