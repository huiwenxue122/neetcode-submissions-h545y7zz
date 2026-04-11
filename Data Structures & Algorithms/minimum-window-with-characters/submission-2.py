class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        window = {}
        have, total_need = 0, len(need)
        res = ""
        res_len = float('inf')
        l = 0
        
        for r in range(len(s)):
            # 加入右边字符
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            # 这个字符是否刚好满足要求
            if c in need and window[c] == need[c]:
                have += 1
            
            # 窗口合法，尝试缩小
            while have == total_need:
                # 记录结果
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]
                
                # 移出左边字符
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        return res