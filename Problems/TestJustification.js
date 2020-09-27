/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    const result = [[]];
    result[0].letters = 0;
    for (let word of words) {
        let row = result[result.length - 1];
        if (row.length && row.letters + row.length + word.length > maxWidth) {
            result.push([]);
            row = result[result.length - 1];
            row.letters = 0;
        }
        row.push(word);
        row.letters += word.length;
    }
    for (let i = 0; i < result.length; i++) {
        let row = result[i];
        if (row.length === 1 || i === result.length - 1) {
            result[i] = row.join(' ') + ' '.repeat(maxWidth - row.letters - row.length + 1);
            continue;
        }
        let line = row[0];
        let spaces = maxWidth - row.letters;
        let minSpaces = ' '.repeat(Math.floor(spaces / (row.length - 1)));
        let addSpace = spaces % (row.length - 1);
        for (let j = 1; j < row.length; j++) {
            line += minSpaces + (j <= addSpace ? ' ' : '') + row[j];
        }
        result[i] = line;
    }
    return result;
};
