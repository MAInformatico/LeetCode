class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new LinkedList<>();
        if (n < k || k == 0) return result;
        
        result = combine(n - 1, k - 1);
        if (result.isEmpty()) {
            result.add(new LinkedList<Integer>());
        }
        for (List<Integer> list : result) {
            list.add(n);
        }
        result.addAll(combine(n - 1, k));
        return result;
    }
}
