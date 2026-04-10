class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        if len(s) != len(t):
            return False
        for char in s:
            list.append(char)
        for ch in t:
            if ch in list:
                list.remove(ch)
            else:
                return False
        return True
