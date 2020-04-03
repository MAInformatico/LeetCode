class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if($x<0){
            return false;
        }
        $last=0;
        $aux=$x;
        while($x){
            $last=$last*10+$x%10;
            $x=intval(floor($x/10));
        }
        if($last==$aux) {
            return true;
        }else {
            return false;
        }
    }
}
