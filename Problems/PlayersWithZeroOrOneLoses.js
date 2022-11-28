/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
    var allPlayer = {};
    var lose = {};
  
    for(var i = 0; i<matches.length; i++){
        if(lose[matches[i][1]])
            lose[matches[i][1]]++;
        else    
            lose[matches[i][1]] = 1
    
        if(!allPlayer[matches[i][0]])
            allPlayer[matches[i][0]] = 1
        if(!allPlayer[matches[i][1]])
            allPlayer[matches[i][1]] = 1        
    }
    
    var first = [], second = [];
    for(var key in allPlayer){
        if(!lose[key])
            first.push(key);
        if(lose[key] == 1)
            second.push(key);
    }
        
    return [first, second];
    
};
