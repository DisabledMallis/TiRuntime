import parser;
import interpreter;
import result;

def shellInput():
	text = input(":");
	return text;

def shellLoop():
	while True:
		text = shellInput();
		tokens = parser.parse(text);
		result = interpreter.eval(tokens);
		result.printResult();