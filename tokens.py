class Token:
	def __init__(self, text, topByte, bottomByte=None):
		self.text = text
		self.topByte = topByte
		self.bottomByte = bottomByte
	
	def __str__(self):
		return "Token: \""+self.getText()+"\", Top: "+str(self.getTopByte())+("" if (self.getBottomByte() == None) else ", Bottom: "+str(self.getBottomByte()));

	def getText(self):
		return self.text;
	
	def getTopByte(self):
		return self.topByte;
	def getBottomByte(self):
		return self.bottomByte;

	def getBytes(self):
		if self.bottomByte == None:
			return self.getTopByte();
		else:
			return [self.getTopByte(), self.getBottomByte()];

allTokens = [];

def createToken(text, topByte, bottomByte=None):
	global allTokens;
	token = Token(text, topByte, bottomByte);
	allTokens.append(token);
	return token;

NUM_0 = createToken("0", 0x30);
NUM_1 = createToken("1", 0x31);