class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict=[]
        for s in strs:
            tempDict = {}
            for i in s:
                if i not in tempDict:
                    tempDict[i]=1
                else:
                    tempDict[i] = tempDict[i]+1
            strDict.append(tempDict)
        groupAnag = []
        grouped=[]
        for i in range(len(strDict)):
            if i not in grouped:
                tempList=[]
                tempList.append(strs[i])
                grouped.append(i)
                if i <len(strDict)-1:
                    for j in range(i+1,len(strDict)):
                        if strDict[i]==strDict[j]:
                            if j not in grouped:
                                tempList.append(strs[j])
                                grouped.append(j)
                groupAnag.append(tempList)
        return groupAnag

        