var climbStairs = function(n) {
    var f1 = 2;
    var f2 = 1;
    if(n == 1) {
        return f2;
    } else if(n == 2) {
        return f1;
    }
    var fn;
    for(var i = 3; i <= n; i++) {
        fn = f1 + f2;
        f2 = f1;
        f1 = fn;
    }
    return fn;
};
