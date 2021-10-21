from antlr.TiBasicListener import TiBasicListener;

class Interpreter(TiBasicListener):
	def enterDisp(self, ctx):
		print(ctx.token)