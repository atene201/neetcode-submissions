class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2 pointers, read and one writing
        write = 0 # idx of last seen value that matches val
        for read in range(len(nums)):
            print(nums)
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        
        # this last for loop not necessary just for placeholders
        for i in range(write, len(nums)):
            nums[i] = 0
        print(nums)
        return write

            
        
                
        