class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        if ($prices == null || sizeof($prices) == 0)
            return 0;
        $maxResult = 0;
        for ($i = 0; $i < sizeof($prices)-1; $i++){
            $maxResult += max($prices[$i+1]-$prices[$i], 0);
        }
        return $maxResult;
    }
}
