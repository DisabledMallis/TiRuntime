# Ti-Basic expressions
# This class is constructed via a text
# expressions are recursive
# All of the following are valid expressions
# expression+expression - ADD
# expression-expression - SUB
# expression*expression - MUL
# expression/expression - DIV
# expression^expression - POW
# (expression)			- PAR
# numbers				- NUM
# variables				- VAR
# expressions follow PEMDAS

# This class parses an expression

digits = range(0,10);
class Expression:
	def __init__(self, text):
		parsingText = text;
		digitText = "";
		while digits.index(parsingText[0]) != -1:
			digitText += parsingText[0];
			parsingText = parsingText[1:];