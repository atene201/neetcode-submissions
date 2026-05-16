class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # 2 pointers, read and one writing

        write = 0
        for read in range(len(nums)):
            print(nums)
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        
        for i in range(write, len(nums)):
            nums[i] = 0
        print(nums)
        return write

            
        
                
        