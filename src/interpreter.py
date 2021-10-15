import result;

def evalExpr(tokens):
	

def eval(tokens):
	for i in range(0, len(tokens)):
		token = tokens[i];
		token.runAction(tokens, i);
	return result.UNKNOWN;