/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function(edges, node1, node2) {
    const leng = edges.length;
    const DFS = (i, dist)=>{
        const checked = new Set();
        let len = 0;
        while(i != -1){
            dist[i] = len++;
            checked.add(i);
            if(checked.has(edges[i])) break;
            i = edges[i];
        }
    }
    const num1Dist = Array(leng).fill(-1);
    const num2Dist = Array(leng).fill(-1);
    DFS(node1, num1Dist);
    DFS(node2, num2Dist);
    let maximum = Number.MAX_SAFE_INTEGER;
    let result = -1;
    for(let i = 0; i < leng; ++i){
        if(num1Dist[i] == -1 || num2Dist[i] == -1) continue;
        if(Math.max(num1Dist[i], num2Dist[i]) < maximum){
            result = i;
            maximum = Math.max(num1Dist[i], num2Dist[i]);
        }
    }
    return result;
};
