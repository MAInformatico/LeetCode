/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
        if (digits.length === 0) return [];
    
	var dictmap = {
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"]
	};
    var combinations = [''];
    
    for (var i = 0; i < digits.length; i++) { //generate combinations
        var digit = digits[i];
        var letters = dictmap[digit];
        var tempArray = [];
        
        if (letters === undefined) continue;
        
        for (var j = 0; j < letters.length; j++) {
            var letterToAdd = letters[j];
            for (var k = 0; k < combinations.length; k++) {
                var combination = combinations[k];
                tempArray.push(combination + letterToAdd);
            }
        }
        combinations = tempArray;
    }
    return combinations;
};
