class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix sol
        total_sum = sum(nums)
        prefix_sum = [0] * (len(nums) + 1) # use a 1-indexed arr

        for idx in range(1, len(nums)+1):
            prefix_sum[idx] = nums[idx-1] + prefix_sum[idx-1] # use the prev sum
            right_sum = total_sum - prefix_sum[idx]
            if right_sum == prefix_sum[idx-1]:
                return idx-1

        print(prefix_sum)
        return -1
