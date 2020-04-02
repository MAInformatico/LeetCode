class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $result = 0;
        $arr = [];
        for ($i = $j = 0, $l = strlen($s); $j < $l; $j++) {
            if (isset($arr[$s[$j]])) {
                $i = max($i, $arr[$s[$j]] + 1);
            }
            $result = max($result, $j - $i + 1);
            $arr[$s[$j]] = $j;
        }
        return $result;
    }
}
