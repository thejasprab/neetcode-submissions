class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]]+=1
        topKFreq=[]
        for i in range(k):
            maxFreq =0
            maxFreqInd = 0 
            for j in numsDict:
                if numsDict[j] > maxFreq:
                    maxFreq = numsDict[j]
                    maxFreqInd = j
            topKFreq.append(maxFreqInd)
            numsDict[maxFreqInd]=0
        return topKFreq
        