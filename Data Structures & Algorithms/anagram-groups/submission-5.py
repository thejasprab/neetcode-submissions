class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convertStrToDict(s):
            sDict={}
            if s == "":
                sDict[""] = 1
                return sDict
            for i in range(len(s)):
                if s[i] in sDict:
                    sDict[s[i]]+=1
                else:
                    sDict[s[i]] = 1
            return sDict
        
        strsDicts,strsAdded=[],[]
        for i in range(len(strs)):
            strsDicts.append(convertStrToDict(strs[i]))
            strsAdded.append(False)
        print(strsDicts)
        i=0
        retStrs=[]
        while i<len(strs):
            if strsAdded[i] == False:
                strsAdded[i] = True
                j=i+1
                matchStrs=[]
                matchStrs.append(strs[i])
                while j< len(strs):
                    if strsAdded[j] == False and strsDicts[j]==strsDicts[i]:
                        strsAdded[j] = True
                        matchStrs.append(strs[j])
                    j+=1
                retStrs.append(matchStrs)
            i+=1
        return retStrs