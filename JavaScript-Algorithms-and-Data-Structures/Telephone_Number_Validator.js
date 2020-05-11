function telephoneCheck(str) {
  
	if (str[0] === "1") {
		str = str.slice(1, str.length);
	} if (str[0] === " ") {
		str = str.slice(1, str.length);
	}
	if (str.match(/\d/g).length !== 10) {
		return false;
	} else if (/^([(]\d{3}[)]|\d{3})[ -]{0,1}\d{3}[ -]{0,1}\d{4}/.test(str)) {
	
		return true;
	} else {
		return false;
	}
}

telephoneCheck("1 555-555-5555");