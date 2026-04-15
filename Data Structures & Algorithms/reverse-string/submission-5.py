class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        m=n-1
        for i in range (0,n):
            if(i<m):
                temp = s[i]
                s[i] = s[m]
                s[m] = temp
                m -=1
            else:
                break