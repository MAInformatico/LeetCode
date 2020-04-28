class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNumbers($nums) {
        $result = 0;
        foreach ($nums as $i) {
            if (strlen ($i) % 2 == 0) 
                $result++;
        }
        return $result;
    }
}
