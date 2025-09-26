class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        c=0
        for char in s:
            if char!=' ':
                c+=1
            elif c>0:
                break
        return c