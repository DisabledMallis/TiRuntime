export module Input {
	var unflushedInput: String = "";
	export function input(text: String) {
		unflushedInput = text;
	}

	export function poll() {
		if(unflushedInput != "") {
			var retText = unflushedInput;
			unflushedInput = "";
			return retText;
		}
		return null;
	}
}