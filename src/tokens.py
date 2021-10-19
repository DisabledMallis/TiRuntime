import runtime.interpreter as interpreter;

class Token:
	def __init__(self, text, topByte, bottomByte=None, action=None):
		self.text = text
		self.topByte = topByte
		self.bottomByte = bottomByte
		self.action = action;
	
	def __str__(self):
		return "Token: \""+self.getText()+"\", Top: "+str(hex(self.getTopByte()))+("" if (self.getBottomByte() == None) else ", Bottom: "+str(self.getBottomByte()));

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
	
	def runAction(self, tokens):
		if self.action == None:
			print("Token "+self.getText()+" has no action");
			return True;
		else:
			return self.action(self, tokens);

class Digit(Token):
	def __init__(self, text):
		self.text = text;
		self.topByte = int(text)+0x30;
		self.bottomByte = None;
		self.action = None;
	
	def runAction(self, tokens):
		# Digits have no actions, they should be parsed by expressions and such of other actions
		return True;

allTokens = [];

def defaultAction(token, tokens):
	#print("Token "+token.getText()+" runs with the default action");
	return True;

def createDigit(text):
	global allTokens;
	digit = Digit(text);
	allTokens.append(digit);
	return digit;
def createToken(text, topByte, bottomByte=None, action=defaultAction):
	global allTokens;
	token = Token(text, topByte, bottomByte, action);
	allTokens.append(token);
	return token;

def displayAction(token, tokens):
	output = ""
	result, output = interpreter.evalExpr(tokens);
	print(output);
	return True;
DISP = createToken("Disp", 0x0, action=displayAction);
ADD = createToken("+", 0x0);
SUB = createToken("-", 0x0);
MUL = createToken("*", 0x0);
DIV = createToken("/", 0x0);
BLANK = createToken(" ", 0x0);
QUOTE = createToken("\"", 0x0);
#Registers tokens for all digits 0-9
NUM = [];
for i in range(0, 10):
	NUM.append(createDigit(str(i)));
#Registers tokens for all letters A-Z
LETTER = [];
for i in range(0, 26):
	LETTER.append(createToken(chr(i+0x41), i+0x41));
for i in range(0, 26):
	LETTER.append(createToken(chr(i+0x61), 0x0));
#NUM_0 = createToken("0", 0x30);
#NUM_1 = createToken("1", 0x31);
#NUM_2 = createToken("2", 0x32);
#NUM_3 = createToken("3", 0x33);
#NUM_4 = createToken("4", 0x34);
#NUM_5 = createToken("5", 0x35);
#NUM_6 = createToken("6", 0x36);
#NUM_7 = createToken("7", 0x37);
#NUM_8 = createToken("8", 0x38);
#NUM_9 = createToken("9", 0x39);