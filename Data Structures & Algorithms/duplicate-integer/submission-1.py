class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for i in nums:
            if i not in numsDict:
                numsDict[i] =0
            else:
                return True
        return False
         