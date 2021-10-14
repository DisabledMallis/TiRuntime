def createToken(text, topByte, bottomByte=0):
	return TiToken(text, topByte, bottomByte)

class TiToken:
	def __init__(self, text, topByte, bottomByte):
		self.text = text
		self.topByte = topByte
		self.bottomByte = bottomByte

