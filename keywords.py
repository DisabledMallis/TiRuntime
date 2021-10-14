# Shell keywords for Ti Basic tokens

class Keyword:
	def __init__(self, regex, stringRep, bytes):
		self.regex = regex
		self.stringRep = stringRep
		self.bytes = bytes