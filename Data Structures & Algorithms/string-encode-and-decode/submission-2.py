class Solution:

    def encode(self, strs: List[str]) -> str:
        encdStr = ""
        for string in strs: 
            encdStr+=str(len(string))+"#"+string
        return encdStr   

    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i=0
        while i <len(s):
            j=i+1
            while s[j] != "#":
                j=j+1
            strLen = int(s[i:j])
            i=j+1
            j=i+strLen
            decodedStr.append(s[i:j])
            i=j
        return decodedStr

        