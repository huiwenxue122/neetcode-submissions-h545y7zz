class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in set(nums):          # 用 set 去重，少算几次
            count = 0                  # 每个 num 重新计数！
            for i in nums:
                if i == num:
                    count += 1
            if count > n // 2:
                return num