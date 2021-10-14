import { Tokens } from "../tokens";
import { TokenAction } from "../tokenAction";

export class DispAction extends TokenAction {
	run(token: Tokens.Token) {
		console.log("Display token!");
		super.run(token);
	}
};