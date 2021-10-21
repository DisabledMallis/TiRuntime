import tokens;
from antlr4 import *;
from antlr.TiBasicLexer import TiBasicLexer;
from antlr.TiBasicParser import TiBasicParser;
from runtime.interpreter import Interpreter;


def parse(text):
	lexer = TiBasicLexer(text);
	stream = CommonTokenStream(lexer);
	parser = TiBasicParser(stream);
	tree = parser.script();
	walker = ParseTreeWalker(tree);

	interpreter = Interpreter();

	walker.walk(interpreter, tree);
	
	return None;