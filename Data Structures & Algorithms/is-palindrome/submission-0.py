class Solution:
    def isPalindrome(self, s: str) -> bool:
        strAlnum = "".join( char for char in s if char.isalnum())
        strAlnum = strAlnum.lower()
        i,j = 0,len(strAlnum)-1
        
        while i< len(strAlnum):

            if(strAlnum[i]!=strAlnum[j]):
                return False
            
            i+=1
            j-=1
        
        return True
        