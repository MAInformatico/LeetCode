class Solution {

    /**
     * @param Integer $columnNumber
     * @return String
     */
    function convertToTitle($n) {        
        $alphabet = array('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z');
    $result="";
    
    while($n){
        $n = $n - 1;
        $result = $alphabet[$n % 26] . $result;
        $n = intdiv($n, 26);
    }
  
    return $result;
    }
}
