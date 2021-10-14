export class Token {

	topByte: byte;
	bottomByte: byte;
	text: String;

	public constructor(topByte, text) {
		this(topByte, 0, text);
	}
	public constructor(topByte, bottomByte, text) {
		this.topByte = topByte;
		this.bottomByte = bottomByte;
		this.text = text;
	}
};