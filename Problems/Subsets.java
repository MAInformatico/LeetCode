class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        
        for(int currentNum : nums){
            int n = result.size();
            for(int i = 0; i<n; i++){
                List<Integer> set = new ArrayList<>(result.get(i));
                set.add(currentNum);
                result.add(set);
            }            
        }
        return result;
    }
}
