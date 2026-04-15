class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        m = n-1
        for i in range (0,n):
            if(s[i]==s[m]):
                m -=1
            else:
                return False
        return True