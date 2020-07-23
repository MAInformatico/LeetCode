class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function jump($nums) {
        if(count($nums) < 2) return 0;
        
        $next=0;
        $aux=0;
        $countJump=0;
        
        for($i=0;$i<count($nums);++$i) {
            $aux = max($aux,$i+$nums[$i]);
            if ($aux >= count($nums)-1) return $countJump+1;
            
            if($i === $next) {
                $next = $aux;
                $countJump++;
            }
        }
        return 0;
    }
}
