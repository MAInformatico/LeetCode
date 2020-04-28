class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxConsecutiveOnes($nums) {
        $count = 0;        
        $result = 0;  

        for ($i = 0; $i < sizeof($nums); $i++) { 
            if ($nums[$i] == 0) 
                $count = 0; 
            else{ 
                $count++; 
                $result = max($result, $count); 
            } 
        } 
        return $result; 
    }
}
