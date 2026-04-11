class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        count1 = {}
        count2 = {}
        
        # 统计 s1 的频次
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        # 固定窗口滑动
        for r in range(len(s2)):
            # 加入右边字符
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            
            # 窗口超出长度，移出左边字符
            if r >= len(s1):
                l = r - len(s1)
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
            
            # 判断
            if count1 == count2:
                return True
        
        return False

                

            