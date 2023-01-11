/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    const adjacentList = Array.from(Array(n), () => new Array());
    for(const edge of edges){
        adjacentList[edge[0]].push(edge[1]);
        adjacentList[edge[1]].push(edge[0]);
    }
    const DFS = (i, p)=>{
        let pathLen = 0;
        for(const j of adjacentList[i]){
            if(j == p) continue;
            pathLen += DFS(j, i);
        }
        if(i == 0) return pathLen;
        return pathLen > 0 || hasApple[i]? pathLen+2 : 0;
    }
    return DFS(0,-1);
};
