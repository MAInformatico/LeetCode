class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        foreach($nums as $i=>$v){
            foreach($nums as $i1=>$v1){
                if(($v+$v1)==$target && $i1!=$i){
                    return [$i,$i1];
                }
            }  
        }
    }
}
