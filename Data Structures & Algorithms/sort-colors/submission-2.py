class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # dutch flag 
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        left, right = 0, len(nums)-1
        mid = 0

        while mid <= right:
            if nums[mid] == 0:
                swap(left, mid)
                left += 1
            elif nums[mid] == 2:
                swap(mid, right)
                right -= 1
                mid -= 1
            mid += 1



            
        


        