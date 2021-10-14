def createToken(text, topByte, bottomByte=0):
	return TiToken(text, topByte, bottomByte)

class TiToken:
	def __init__(self, text, topByte, bottomByte):
		self.text = text
		self.topByte = topByte
		self.bottomByte = bottomByte

NUM_0 = createToken("0", 0x30)
NUM_1 = createToken("1", 0x31)
NUM_2 = createToken("2", 0x32)
NUM_3 = createToken("3", 0x33)
NUM_4 = createToken("4", 0x34)
NUM_5 = createToken("5", 0x35)
NUM_6 = createToken("6", 0x36)
NUM_7 = createToken("7", 0x37)
NUM_8 = createToken("8", 0x38)
NUM_9 = createToken("9", 0x39)