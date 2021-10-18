import runtime.parser as parser;
import runtime.interpreter as interpreter;
#import runtime.result as result;

def shellInput():
	text = input(":");
	return text;

def shellLoop():
	while True:
		text = shellInput();
		tokens = parser.parse(text);
		result = interpreter.evalLine(tokens);
		result.printResult();