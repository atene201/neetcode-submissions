class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # is n/3 interge divison?

        count = defaultdict(int)
        baseline = len(nums) // 3
        res = []
        for num in nums:
            count[num] += 1
            if count[num] > baseline and num not in res:
                res.append(num)
        
        return res

        


        