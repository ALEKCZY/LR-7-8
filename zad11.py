def function(string: str) -> str:
	if len(string) > 10:
		return string[:6]
	else:
		return string + 'o' * (12-len(string)