class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer,Integer> twoSumHash = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(twoSumHash.get(target-nums[i])!=null){
                result[1]=i;
                result[0]=twoSumHash.get(target-nums[i]);
            }
            twoSumHash.put(nums[i],i);
        }
        return result;
    }
}
