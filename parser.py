import tokens;

def parse(text):
	tokenSet = [];
	allTokens = tokens.allTokens;

	parsingText = text;
	while parsingText != "":
		for i in range(0, len(allTokens)):
			token = allTokens[i];
			tkStr = token.getText();
			if parsingText[0:len(tkStr)] == tkStr:
				tokenSet.append(token);
				parsingText = parsingText[len(tkStr):];
	
	return tokenSet;