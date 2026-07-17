class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> inputArrayHash = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if(inputArrayHash.containsKey(nums[i])){
                return true;
            }
            else {
                inputArrayHash.put(nums[i],1);
            }
        }
        return false;
    }
}