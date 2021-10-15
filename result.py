class Result:
	def __init__(self, code, message):
		self.code = code;
		self.message = message;
	def __str__(self):
		return "Result code: "+str(self.code)+"\nMessage: "+self.message;
	def printResult(self):
		print(str(self));

SUCCESS = Result(0, "Success");
UNKNOWN = Result(1, "Unknown error occoured");