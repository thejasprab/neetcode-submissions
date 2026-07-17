class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resInd = []
        i=0
        while i<len(nums)-1:
            sumCheck = target -( nums[i])
            if sumCheck in nums[i+1:]:
                j = nums.index(sumCheck,i+1,len(nums))
                resInd.append(i)
                resInd.append(j)
                return resInd
            i=i+1
        return resInd