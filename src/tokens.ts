import { Action } from "./action";
import { TokenAction } from "./tokenAction";

export module Tokens {
	//Token list for iteration
	export var allTokens: Token[] = [];

	//Token class
	export class Token {
		public static registerToken(text: String, topByte: number, bottomByte?: number, action?: TokenAction) {
			var theAction: TokenAction = null;
			if(action != null) {
				theAction = action;
			}
			var token = new Token(text, theAction, topByte, bottomByte as any);
			allTokens.push(token);
			return token;
		}
	
		//Class features
		private text: String;
		private topByte: number;
		private bottomByte?: number;
		private action?: TokenAction;
	
		public constructor(text: String, action: TokenAction, topByte: number);
		public constructor(text: String, action: TokenAction, topByte: number, bottomByte: number);
		public constructor(text: String, action: TokenAction, topByte: number, bottomByte?: number) {
			this.topByte = topByte;
			this.bottomByte = bottomByte;
			this.text = text;
			this.action = action;
		};	
	};

	//Token instances
	export var TO_DMS = Token.registerToken("TO_DMS", 0x1);
	export var TO_DEC = Token.registerToken(">DEC", 0x2);
	export var TO_FRAC = Token.registerToken(">FRAC", 0x3);
	export var STORE = Token.registerToken("->", 0x4);
	export var BOXPLOT = Token.registerToken("BOXPLOT", 0x5);
	export var OPEN_SQUARE_BRACKET = Token.registerToken("[", 0x6);
	export var CLOSE_SQUARE_BRACKET = Token.registerToken("]", 0x7);
	export var OPEN_CURLEY_BRACKET = Token.registerToken("{", 0x8);
	export var CLOSE_CURLEY_BRACKET = Token.registerToken("}", 0x9);
	export var OPEN_BRACKET = Token.registerToken("(", 0x10);
	export var CLOSE_BRACKET = Token.registerToken(")", 0x11);
	export var BLANK = Token.registerToken(" ", 0x29);
	export var QUOTE = Token.registerToken("\"", 0x2A);
	export var COMMA = Token.registerToken(",", 0x2B);
	export var EXCLAMATION_MARK = Token.registerToken("!", 0x2D);
	export var NUM_0 = Token.registerToken("0", 0x30);
	export var NUM_1 = Token.registerToken("1", 0x31);
	export var NUM_2 = Token.registerToken("2", 0x32);
	export var NUM_3 = Token.registerToken("3", 0x33);
	export var NUM_4 = Token.registerToken("4", 0x34);
	export var NUM_5 = Token.registerToken("5", 0x35);
	export var NUM_6 = Token.registerToken("6", 0x36);
	export var NUM_7 = Token.registerToken("7", 0x37);
	export var NUM_8 = Token.registerToken("8", 0x38);
	export var NUM_9 = Token.registerToken("9", 0x39);
	export var PERIOD = Token.registerToken(".", 0x3A);
	export var OR = Token.registerToken("OR", 0x3A);
	export var XOR = Token.registerToken("XOR", 0x3D);
	export var COLON = Token.registerToken(":", 0x3E);
	export var NEWLINE = Token.registerToken("\n", 0x3F);
	export var LETTER_A = Token.registerToken("A", 0x41);
	export var LETTER_B = Token.registerToken("B", 0x42);
	export var LETTER_C = Token.registerToken("C", 0x43);
	export var LETTER_D = Token.registerToken("D", 0x44);
	export var LETTER_E = Token.registerToken("E", 0x45);
	export var LETTER_F = Token.registerToken("F", 0x46);
	export var LETTER_G = Token.registerToken("G", 0x47);
	export var LETTER_H = Token.registerToken("H", 0x48);
	export var LETTER_I = Token.registerToken("I", 0x49);
	export var LETTER_J = Token.registerToken("J", 0x4A);
	export var LETTER_K = Token.registerToken("K", 0x4B);
	export var LETTER_L = Token.registerToken("L", 0x4C);
	export var LETTER_M = Token.registerToken("M", 0x4D);
	export var LETTER_N = Token.registerToken("N", 0x4E);
	export var LETTER_O = Token.registerToken("O", 0x4F);
	export var LETTER_P = Token.registerToken("P", 0x50);
	export var LETTER_Q = Token.registerToken("Q", 0x51);
	export var LETTER_R = Token.registerToken("R", 0x52);
	export var LETTER_S = Token.registerToken("S", 0x53);
	export var LETTER_T = Token.registerToken("T", 0x54);
	export var LETTER_U = Token.registerToken("U", 0x55);
	export var LETTER_V = Token.registerToken("V", 0x56);
	export var LETTER_W = Token.registerToken("W", 0x57);
	export var LETTER_X = Token.registerToken("X", 0x58);
	export var LETTER_Y = Token.registerToken("Y", 0x59);
	export var LETTER_Z = Token.registerToken("Z", 0x5A);
	export var MATRIX_A = Token.registerToken("[A]", 0x5C, 0x0);
	export var MATRIX_B = Token.registerToken("[B]", 0x5C, 0x1);
	export var MATRIX_C = Token.registerToken("[C]", 0x5C, 0x2);
	export var MATRIX_D = Token.registerToken("[D]", 0x5C, 0x3);
	export var MATRIX_E = Token.registerToken("[E]", 0x5C, 0x4);
	export var MATRIX_F = Token.registerToken("[F]", 0x5C, 0x5);
	export var MATRIX_G = Token.registerToken("[G]", 0x5C, 0x6);
	export var MATRIX_H = Token.registerToken("[H]", 0x5C, 0x7);
	export var MATRIX_I = Token.registerToken("[I]", 0x5C, 0x8);
	export var MATRIX_J = Token.registerToken("[J]", 0x5C, 0x9);
	export var LIST1 = Token.registerToken("LIST1", 0x5D, 0x0);
	export var LIST2 = Token.registerToken("LIST2", 0x5D, 0x1);
	export var LIST3 = Token.registerToken("LIST3", 0x5D, 0x2);
	export var LIST4 = Token.registerToken("LIST4", 0x5D, 0x3);
	export var LIST5 = Token.registerToken("LIST5", 0x5D, 0x4);
	export var LIST6 = Token.registerToken("LIST6", 0x5D, 0x5);
	export var PRGM = Token.registerToken("prgm", 0x5F);
	export var EQUALS = Token.registerToken("=", 0x6A);
	export var LESS_THAN = Token.registerToken("<", 0x6B);
	export var GREATER_THAN = Token.registerToken(">", 0x6C);
	export var LESS_THAN_OR_EQUAL = Token.registerToken("<=", 0x6D);
	export var GREATER_THAN_OR_EQUAL = Token.registerToken(">=", 0x6E);
	export var NOT_EQUAL = Token.registerToken("!=", 0x6F);
	export var ADD = Token.registerToken("+", 0x70);
	export var SUBTRACT = Token.registerToken("-", 0x71);
	export var MULTIPLY = Token.registerToken("*", 0x82);
	export var DIVIDE = Token.registerToken("/", 0x83);
	export var CONST_PI = Token.registerToken("pi", 0xAC);
	export var NEGATE = Token.registerToken("-", 0xB0);
	export var CONST_E = Token.registerToken("e", 0xBB, 0x31);
	export var AND = Token.registerToken("&", 0xBB, 0xD4);
	export var IF = Token.registerToken("IF", 0xCE);
	export var THEN = Token.registerToken("THEN", 0xCF);
	export var END = Token.registerToken("END", 0xD4);
	export var INPUT = Token.registerToken("INPUT", 0xDC);
	export var DISP = Token.registerToken("DISP", 0xDE, null, Action.dispAction);
	export var CLR_LIST = Token.registerToken("CLR_LIST", 0xFA);
};
