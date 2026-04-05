class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        last = {}

        for r in range(len(s)):
            if s[r] in last:
                l = max(last[s[r]] + 1, l)
            last[s[r]] = r
            res = max(res, r - l + 1)
        return res            
        