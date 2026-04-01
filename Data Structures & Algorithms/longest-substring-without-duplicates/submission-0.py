class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        setr = set()
        l = 0
        r = 1
        for r in range(len(s)):
            while s[r] in setr:
                setr.remove(s[l])
                l += 1
            setr.add(s[r])
            res = max(res, r - l + 1)
        return res
        