source = open("source.bas", "r").read()

class Lexer:

	def tokenize_Statement(self, expr):

		tokLen = len(expr)
		token = ""
		i = 0
		
		while i < tokLen:

			if (expr[0].isupper() == True):
				token += expr[0]
				del expr[0]

			i += 1

		if (token == "PRINT"):
			print "found print"  	

		return 1	

	def tokenize_Symbol(self, expr):

		if (expr[0] == " "):
			del expr[0]

		elif (expr[0].isupper):
			self.tokenize_Statement(expr)	 

lexer = Lexer()
code = list(source)
lexer.tokenize_Statement(code)			