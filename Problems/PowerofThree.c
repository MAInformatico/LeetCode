bool isPowerOfThree(int n){
    if (n <= 0 || n==2) return false;
    if (n == 1) return true;    
    bool result = true;
    while (n > 1){            
        if (n % 3 != 0 || n==2) { result = false; break; }
        n /= 3;
    }
    return result;
}
