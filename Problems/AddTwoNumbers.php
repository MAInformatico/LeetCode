/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $result=new ListNode($this->res + $l1->val + $l2->val);
        if($this->res=intval($result->val >9)){
            $result->val -=10;
        }
        $result->next=(!$this->res && is_null($l1->next) && is_null($l2->next) )?null:$this->addTwoNumbers($l1->next,$l2->next);
        return $result;
    }
}
