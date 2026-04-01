class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            count = nums.count(num)
            if count > n // 2:
                return num