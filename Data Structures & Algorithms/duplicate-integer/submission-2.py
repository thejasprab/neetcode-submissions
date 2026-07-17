class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict={}
        for i in nums:
            if i not in numsDict:
                numsDict[i]=1
            else:
                numsDict[i] = numsDict[i]+1
        for i in numsDict.keys():
            if numsDict[i] !=1:
                return True
        return False
         