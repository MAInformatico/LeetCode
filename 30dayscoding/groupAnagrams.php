class Solution {

    /**
     * @param String[] $strs
     * @return String[][]
     */
    function groupAnagrams($strs) {
        $result=[];
        foreach($strs as $str){
            $aux=str_split($str);
            sort($aux);
            $temp=implode(' ',$aux).''; //join array elements on a string
            $result[$temp][]=$str;
        }
        return $result;
    }
}
