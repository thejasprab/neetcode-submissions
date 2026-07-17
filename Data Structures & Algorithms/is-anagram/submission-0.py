class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}

        for i in s:
            if i not in dictS:
                dictS[i] = 1
            else:
                dictS[i] = dictS[i] +1
        for i in t:
            if i not in dictT:
                dictT[i] = 1
            else:
                dictT[i] = dictT[i] +1
        
        if dictS == dictT:
            return True
        else:
            return False
        
        