import result;

def eval(tokens):
	for i in range(0, len(tokens)):
		token = tokens[i];
		token.runAction();
	return result.UNKNOWN;