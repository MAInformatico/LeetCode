var UndergroundSystem = function() {
    this.average = new Map();
    this.train = new Map();    
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    this.train.set(id, [stationName, t]);    
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    const [start, s] = this.train.get(id);
    const key = [start, stationName].join();
    if(this.average.has(key)){
        let [average, count] = this.average.get(key);
        this.average.set(key, [average * (count/++count) + ((t-s)/count), count]);
    }
    else{
        this.average.set(key, [(t-s),1]);
    }
    this.train.delete(id);
};

/** 
 * @param {string} startStation 
 * @param {string} endStation
 * @return {number}
 */
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    return this.average.get([startStation, endStation].join())[0];
};

/** 
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */
