import tokens;

def parse(text):
	tokenSet = [];
	allTokens = tokens.allTokens;

	parsingText = text;
	while parsingText != "":
		parsedToken = False;
		for i in range(0, len(allTokens)):
			token = allTokens[i];
			tkStr = token.getText();
			if parsingText[0:len(tkStr)] == tkStr:
				tokenSet.append(token);
				parsingText = parsingText[len(tkStr):];
				parsedToken = True;
		if not parsedToken:
			print("Cannot parse \""+parsingText+"\", unknown token?");
			tokenSet = [];
			break;
	
	return tokenSet;