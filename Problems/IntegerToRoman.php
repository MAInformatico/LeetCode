class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num) {
        $m = array("", "M", "MM", "MMM"); 
        $c = array("", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM"); 
        $x = array("", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"); 
        $i = array("", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"); 
     
        $um = $m[$num / 1000]; 
        $c = $c[($num % 1000) / 100]; 
        $d = $x[($num % 100) / 10]; 
        $u = $i[$num % 10]; 
        $result = $um . $c . $d . $u; 

        return $result;   
        
    }
}
