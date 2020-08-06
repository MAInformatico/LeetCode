class Solution {
    public void sortColors(int[] nums) {
        int itR = 0;
        int itW = 0;
        int itB = nums.length-1;        
        while (itW <= itB) {
            if (nums[itW] == 0) {
                nums[itW] = nums[itR];
                nums[itR] = 0;
                itR++;
                itW++;
            }
            else if (nums[itW] == 1) {
                itW++;
            }
            else {
                nums[itW] = nums[itB];
                nums[itB] = 2;
                itB--;
            }
        }   
    }
}
