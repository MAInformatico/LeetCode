var Trie = function() {
    this.root = {};
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for(let i of word){
        if(!node[i]){
            node[i] ={}
         }
        node = node[i];
    }
    node["isEnd"] = true;
};


/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root; 
    for(let i of word){
        if(node[i]){
            node = node[i];
        }else{
            return false;
        }
    }
    return node["isEnd"] === true;
    
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root; 
    for(let i of prefix){
        if(!node[i]){
            return false;
        }
        node = node[i];
    }
    return true;
};
/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
