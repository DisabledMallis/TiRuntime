import { TokenAction } from "./tokenAction";
import { DispAction } from "./actions/dispAction";

export module Action {
	var tokenActions: Array<TokenAction> = [];

	export function registerAction(action: TokenAction) {
		tokenActions.push(action);
		return action;
	};

	export var dispAction: TokenAction = registerAction(new DispAction());
};