import runtime.interpreter as interpreter;

class Token:
	def __init__(self, text, topByte, bottomByte=None, action=None):
		self.text = text
		self.topByte = topByte
		self.bottomByte = bottomByte
		self.action = action;
	
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
	
	def runAction(self, tokens, index):
		if self.action == None:
			print("Token "+self.getText()+" has no action");
		else:
			return self.action(self, tokens, index);

allTokens = [];

def defaultAction(token, tokens, index):
	print("Token "+token.getText()+" runs with the default action");

def createToken(text, topByte, bottomByte=None, action=defaultAction):
	global allTokens;
	token = Token(text, topByte, bottomByte, action);
	allTokens.append(token);
	return token;

ADD = createToken("+", 0x0);
SUB = createToken("-", 0x0);
MUL = createToken("*", 0x0);
DIV = createToken("/", 0x0);
BLANK = createToken(" ", 0x0);
NUM_0 = createToken("0", 0x30);
NUM_1 = createToken("1", 0x31);
NUM_2 = createToken("2", 0x32);
NUM_3 = createToken("3", 0x33);
NUM_4 = createToken("4", 0x34);
NUM_5 = createToken("5", 0x35);
NUM_6 = createToken("6", 0x36);
NUM_7 = createToken("7", 0x37);
NUM_8 = createToken("8", 0x38);
NUM_9 = createToken("9", 0x39);
def displayAction(token, tokens, index):
	output = ""
	toDisp = tokens[index+1:];
	result, output = interpreter.evalExpr(toDisp);
	print(output);
DISP = createToken("Disp", 0x0, action=displayAction);