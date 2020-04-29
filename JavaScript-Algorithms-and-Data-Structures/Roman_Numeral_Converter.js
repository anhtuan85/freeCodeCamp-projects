function convertToRoman(num) {
	var decimalVal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
	var romanNumeral = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
	var convert_num = "";
	for (let i =0; i < decimalVal.length; i++) {
		while (decimalVal[i] <= num) {
			convert_num += romanNumeral[i];
			num -= decimalVal[i];
		}
	}
	return convert_num;
}

convertToRoman(36);