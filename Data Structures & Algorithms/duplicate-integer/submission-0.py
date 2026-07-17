class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateCheck = {}
        for i in range(len(nums)):
            if nums[i] not in duplicateCheck:
                duplicateCheck[nums[i]] = 0
            else:
                return True
        return False