class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
            $nums = array_flip($nums); 
            $nums = array_flip($nums); 
            $nums= array_values($nums);
    }
}
