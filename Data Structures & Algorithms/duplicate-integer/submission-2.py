class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > 1:
                return True
        
        return False