function palindrome(str) {
	str = str.replace(/[\W_]/gi, "").toLowerCase();
	return str === str.split("").reverse().join("");
}
palindrome("eye");