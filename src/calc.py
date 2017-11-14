source = open("source.bas", "r").read()
contest = list(source)

class Calc:

	def parse_Formula(self, expr):

		result = self.parse_Secondary(expr)

		while (len(expr) > 0):
			del expr[0]
			result += self.parse_Secondary(expr)

		return result	

	def parse_Secondary(self, expr):

		exp1 = self.parse_Primary(expr)

		try:
			while (expr[0] == "+"):
				del[expr[0]]
				exp2 = self.parse_Primary(expr)
				exp1 += exp2

			while (expr[0] == "-"):
				del[expr[0]]
				exp2 = self.parse_Primary(expr)
				exp1 -= exp2	

		except (IndexError):
			return exp1	

		return exp1				


	def parse_Primary(self, expr):

		num1 = self.parse_Dicision(expr)

		try:
			while (expr[0] == "*"):
					del expr[0]
					num2 = self.parse_Dicision(expr)
					num1 *= num2

			while (expr[0] == "/"):
					del expr[0]
					num2 = self.parse_Dicision(expr)
					num1 /= num2		

		except (IndexError):
			return num1	

		return num1			


	def parse_Dicision(self, expr):

		if (expr[0].isdigit()):
			return self.parse_Num(expr)

		elif (expr[0] == "-"):
			del expr[0]

			if (expr[0] == "("):
				del expr[0]
				exp = -self.parse_Secondary(expr)
				del expr[0]
				return exp

			else:	
				return -self.parse_Num(expr)

		elif (expr[0] == "("):
			del expr[0]
			exp = self.parse_Secondary(expr)
			del expr[0]
			return exp
					

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
result = Calc.parse_Formula(calc, contest)
print result




#print expr[expr.index(char):]
		