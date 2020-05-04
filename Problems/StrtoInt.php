class Solution {

    /**
     * @param String $str
     * @return Integer
     */
    function myAtoi($str) {
        $str = trim($str);
        $str = explode('.', $str)[0];
        $str = explode('e', $str)[0];
        $arr = str_split($str);
        while (count($arr)) {
            $num = implode($arr);
            if (is_numeric($num)) {
                return min(max((int) $num, -pow(2,31)), pow(2,31) - 1);
            }
            array_pop($arr);
        }

        return 0;
    }
}
