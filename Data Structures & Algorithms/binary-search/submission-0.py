class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, left, right, target):
        
        if left > right:
            return -1
        mid_idx = int((left + right)/2)
        if nums[mid_idx] == target:
            return mid_idx
        elif target < nums[mid_idx]:
            return self.binary_search(nums, 0, mid_idx-1, target)
        else:
            return self.binary_search(nums, mid_idx+1, right, target)
        

        
        