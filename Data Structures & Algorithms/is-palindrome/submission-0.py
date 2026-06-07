class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        x = []
        
        for ch in s:
            if ch.isalnum():
                x.append(ch)
        i = 0
        j = len(x)-1
        while i<=j:
            if x[i]==x[j]:
                i+=1
                j-=1
            else:
                return False
        return True            
        