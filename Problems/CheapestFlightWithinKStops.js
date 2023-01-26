/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
  //Djikstra's algorithm
    const graph = {};

    for(const [x,y,price] of flights){
        if(!graph[x])
            graph[x] = [];
        graph[x].push([y,price]);
    }

    const dProgramming = Array.from({length: n}, () => Infinity);
    dProgramming[src] = 0;

    const pQueue = [[src,0, k + 1]];

    while(pQueue.length){
        const [x,total, stops] = pQueue.shift();

        if(x === dst)
            continue;
        if(stops === 0)
            continue;
        if(!graph[x])
            continue;

        for(const [y,price] of graph[x]){
            if(dProgramming[y] > total + price){
                dProgramming[y] = total + price;
                pQueue.push([y,total + price, stops-1]);
            }
        }
    }
    return dProgramming[dst] !== Infinity ? dProgramming[dst]: -1;
};
