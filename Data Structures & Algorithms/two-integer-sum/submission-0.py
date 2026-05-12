class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        values = {}

        for i in range(len(nums)):
            perfect_fit = target - nums[i]

            if perfect_fit in values.keys():
                return [values[perfect_fit], i]

            values[nums[i]] = i



        