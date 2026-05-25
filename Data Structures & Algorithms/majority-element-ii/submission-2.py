class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, can2, count1, count2 = None, None, 0, 0

        # find the candidates since there is only 2 possible
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1 = num
                count1 = 1
            elif count2 == 0:
                can2 = num
                count2 = 1
            else: # if there is new num seen
                count1 -= 1
                count2 -= 1
        
        # get count for candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == can1:
                count1 += 1
            if num == can2:
                count2 += 1
        
        # validate candiate
        res = []
        if count1 > (len(nums) // 3):
            res.append(can1)
        if count2 > (len(nums) // 3):
            res.append(can2)

        return res

        


        