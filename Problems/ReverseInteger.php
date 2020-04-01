class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $data=array();
        if($x<0){
                $flag=1;
                $x=-$x;
            }
        
        for($i=0;$x!=0;$i++){
            $data[$i]=$x%10;
            $x=($x-$data[$i])/10;
        }
        
        for($j=0;$j<$i;$j++)
        {
            $result+=$data[$j]*pow(10,$i-$j-1);
        }
        if($flag==1){
            $result=-$result;
        }
        if($result>(pow(2,31)-1)||$result<-pow(2,31)){
            return 0;
        }
        else
            return $result;  
    }
}
