import tokens
import shell

if __name__ == "__main__":
	allTokens = tokens.allTokens;
	for i in range(0, len(allTokens)):
		print(allTokens[i]);
	shell.shellLoop();