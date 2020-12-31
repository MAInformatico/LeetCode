
char findTheDifference(char * s, char * t){
    int dif = 0;
    while (*s) dif ^= *s++;
    while (*t) dif ^= *t++;
    return dif;
}
