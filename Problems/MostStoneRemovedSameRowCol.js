/**
 * @param {number[][]} stones
 * @return {number}
 */
var removeStones = function(stones) {
        const visited = new Set();
        let removed = 0;
      
        const traverse = (row, column) => {
            const key = `${row}-${column}`;

            if (visited.has(key))
              return;

            visited.add(key);
            for (const [x, y] of stones) {                
                if (row === x || column === y)
                  traverse(x, y);
            }
        };

        for (const [x, y] of stones) {
            const key = `${x}-${y}`;

            if (visited.has(key))
              continue;

            traverse(x, y);
            removed++;
        }
      
        return stones.length - removed;  
};
