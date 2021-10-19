class Expression:
	def __init__(self):
		return self;
	def eval(self):
		return 0;

class NumberExpression(Expression):
	def __init__(self, number):
		self.number = number;
	def eval(self):
		return self.number;

class AddExpression(Expression):
	def __init__(self, expressionLeft, expressionRight):
		self.expressionLeft = expressionLeft;
		self.expressionRight = expressionRight;
	def eval(self):
		return self.expressionLeft.eval() + self.expressionRight.eval();

