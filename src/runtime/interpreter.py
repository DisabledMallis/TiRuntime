import runtime.result as result;

def evalExpr(tokens):
	code = "";
	for i in range(0, len(tokens)):
		code += tokens[i].getText();
	complete = eval(code);
	return result.UNKNOWN, complete;

def evalLine(tokens):
	for i in range(0, len(tokens)):
		token = tokens[i];
		token.runAction(tokens, i);
	return result.UNKNOWN;