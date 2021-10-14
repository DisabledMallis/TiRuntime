export class Token {
//Token instances
	public static NUM_0 = Token.registerToken("0", 0x30);
	public static NUM_1 = Token.registerToken("1", 0x31);
	public static NUM_2 = Token.registerToken("2", 0x32);
	public static NUM_3 = Token.registerToken("3", 0x33);
	public static NUM_4 = Token.registerToken("4", 0x34);
	public static NUM_5 = Token.registerToken("5", 0x35);
	public static NUM_6 = Token.registerToken("6", 0x36);
	public static NUM_7 = Token.registerToken("7", 0x37);
	public static NUM_8 = Token.registerToken("8", 0x38);
	public static NUM_9 = Token.registerToken("9", 0x39);


	public static allTokens: Array<Token> = [];
	public static registerToken(text: String, topByte: number, bottomByte?: number) {
		var token = new Token(text, topByte, bottomByte as any);
		Token.allTokens.push(token);
		return token;
	}

//Class features
	private text: String;
	private topByte: number;
	private bottomByte?: number;

	public constructor(text: String, topByte: number);
	public constructor(text: String, topByte: number, bottomByte: number);
	public constructor(text: String, topByte: number, bottomByte?: number) {
		this.topByte = topByte;
		this.bottomByte = bottomByte;
		this.text = text;
	};	
};