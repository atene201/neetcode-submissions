from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # base cases
        if len(nums) == 0 or len(nums) <= 1:
            return False
        
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        for val in m.values():
            if val > 1:
                return True
        
        return False
        