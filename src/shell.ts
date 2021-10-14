import { Input } from "./input";

export class Shell {
	constructor() {
		console.log("TI-Basic shell setup...");
		console.log("Shell ready!");
	}

	runShell() {
		while(true) {
			console.log(":");
			var line = Input.poll();
			if(line != null) {
				console.log(line);
			}
		}
	}
};