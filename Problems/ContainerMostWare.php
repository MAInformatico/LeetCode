class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function maxArea($height) {
        $area = $i = 0;
        $j = sizeof($height)-1;
        
        while (($i!=$j) and $j>0){
            $area = max($area, min($height[$i],$height[$j])*($j-$i));
            if($height[$i]>$height[$j]){
                $j -= 1;
            }
            else{
                $i += 1;
            }
        }
        return $area;
    }
}
