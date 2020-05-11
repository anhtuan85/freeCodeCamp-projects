function rot13(str) {
	const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	var arr = str.split("");
	for (let i =0; i < arr.length; i++) {
		var t = alphabet.indexOf(arr[i]);
		if (t >= 0) {
		arr[i] = alphabet[(t+13)%26];
		}
	}
	return arr.join("");
}

console.log(rot13("SERR PBQR PNZC"));
