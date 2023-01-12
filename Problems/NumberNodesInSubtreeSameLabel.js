/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @return {number[]}
 */
var countSubTrees = function(n, edges, labels) {
    const tree = Array(n).fill().map( _ => [] ), result = []
    labels = labels.split``.map( character => 'abcdefghijklmnopqrstuvwxyz'.indexOf(character) )
    edges.forEach( ( [ x, y ] ) => tree[x].push(y) && tree[y].push(x) )

    const f = ( i = 0, p = null ) => {
        if ( result[i] ) return
        result[i] = [], result[i][labels[i]] = 1
        for ( let j of tree[i] )
            for ( let l in j == p && [] || f(j,i) || result[j] )
                result[i][l] = ~~result[i][l] + result[j][l]
    }

    return f() || result.map( ( n, i ) => n[labels[i]] )
};
