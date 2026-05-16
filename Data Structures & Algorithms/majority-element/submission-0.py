class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = defaultdict(int)

        for num in nums:
            res[num] += 1
        
        max_val = 0;
        for num in res.keys():
            print(f'{num} {res[num]}')
            if res[num] > (len(nums) / 2):
                max_val = num
        
        return max_val