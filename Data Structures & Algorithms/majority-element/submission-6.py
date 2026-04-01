class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        maxcount = 0

        for num in nums:
            count[num] += 1
            if maxcount < count[num]:
                res = num
                maxcount = count[num]
        return res