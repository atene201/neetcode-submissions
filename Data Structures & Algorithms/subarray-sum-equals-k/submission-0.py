class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1}
        current_sum = 0
        res = 0

        for num in nums:
            current_sum += num
            diff = current_sum - k
            res += prefix.get(diff, 0)
            prefix[current_sum] = 1 + prefix.get(current_sum, 0)
        return res
            

