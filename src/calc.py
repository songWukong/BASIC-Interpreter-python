source = open("source.bas", "r").read()

class Calc:

	def parse_Formula(self, source):

		expr = list(source)
		result = self.__parse_Secondary__(expr)

		while (len(expr) > 0):

			if (expr[0] == "\n"):	
				return result
				
			del expr[0]
			result += self.__parse_Secondary__(expr)

		return result	
		

	def __parse_Secondary__(self, expr):

		exp1 = self.__parse_Primary__(expr)

		try:
			while (expr[0] == "+"):
				del[expr[0]]
				exp2 = self.__parse_Primary__(expr)
				exp1 += exp2

			while (expr[0] == "-"):
				del[expr[0]]
				exp2 = self.__parse_Primary__(expr)
				exp1 -= exp2	

		except (IndexError):
			return exp1	

		return exp1				


	def __parse_Primary__(self, expr):

		num1 = self.__parse_Dicision__(expr)

		try:
			while (expr[0] == "*"):
					del expr[0]
					num2 = self.__parse_Dicision__(expr)
					num1 *= num2

			while (expr[0] == "/"):
					del expr[0]
					num2 = self.__parse_Dicision__(expr)
					num1 /= num2		

		except (IndexError):
			return num1	

		return num1			


	def __parse_Dicision__(self, expr):

		if (expr[0].isdigit()):
			return self.parse_Num(expr)

		elif (expr[0] == "-"):
			del expr[0]

			if (expr[0] == "("):
				del expr[0]
				exp = -self.__parse_Secondary__(expr)
				del expr[0]
				return exp

			else:	
				return -self.parse_Num(expr)

		elif (expr[0] == "("):
			del expr[0]
			exp = self.__parse_Secondary__(expr)
			del expr[0]
			return exp

		elif (expr[0] == "\n"):	
				print "new line"	

	def parse_Num(self, expr):

		num = 0
		numLen = len(expr)
		toknum = ""
		i = 0
		
		while i < numLen:

			if (expr[0].isdigit() == False):
				return num	

			toknum += expr[0]
			num = int(toknum)	

			del expr[0]
			i += 1

		return num	

calc = Calc()
result = calc.parse_Formula(source)
print result