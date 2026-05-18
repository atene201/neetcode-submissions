class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # insertion sort

        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                # swap
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                j -= 1
            # nums[i-1] = current



            
        


        