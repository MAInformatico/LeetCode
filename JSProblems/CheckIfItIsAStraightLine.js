/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */

var checkLine = function([[ax,ay],[bx,by],[cx,cy]]){
    return ((by-ay)*(cx-bx) === (cy-by)*(bx-ax));
}

var checkStraightLine = function(coordinates) {
    if(coordinates.length === 2) return true;

    for(let i = 2; i<coordinates.length; i++){
        if(!checkLine([coordinates[0], coordinates[1], coordinates[i]])){
            return false;
        }
    }
    return true;
};
