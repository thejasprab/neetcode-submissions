class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preArr=[0]*len(nums)
        sufArr=[0]*len(nums)
        preArr[0]=sufArr[len(nums)-1] =1
        for i in range(1,len(nums)):
            preArr[i] = nums[i-1] *preArr[i-1]
        for i in range(len(nums)-2,-1,-1):
            sufArr[i] = nums[i+1] * sufArr[i+1]
        result = [0] *len(nums)
        for i in range(len(nums)):
            result[i] = preArr[i]*sufArr[i]
        
        return result
        