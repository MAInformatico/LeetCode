var isValid = function(s) {
    const stack = []
    const dictparens = new Map()
    
    dictparens.set( '(', ')' )
    dictparens.set( '[', ']' )
    dictparens.set( '{', '}' )
    
    for(let i = 0; i<s.length; i++){    
        if(dictparens.has(s[i])) stack.push(s[i])        
        else{
            let top = stack[stack.length-1]
            if (dictparens.get( top )!==s[i]) return false
            else{
                stack.pop()
            }
        }
    }    
    if( stack.length ) return false    
    return true    
};
