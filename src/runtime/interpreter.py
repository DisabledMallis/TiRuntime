import runtime.result as result;
import tokens as tkn;

def sanitizeExpr(tokens):
	if tokens[0] == tkn.NUM[0] or tokens[0] == tkn.BLANK:
		return sanitizeExpr(tokens[1:]);
	return tokens;
def evalExpr(tokens):
	code = "";
	tokens = sanitizeExpr(tokens);
	for i in range(0, len(tokens)):
		code += tokens[i].getText();
	complete = eval(code);
	return result.UNKNOWN, complete;

def evalLine(tokens):
	if tokens[0].runAction(tokens[1:]):
		return result.SUCCESS;
	else:
		return result.UNKNOWN;