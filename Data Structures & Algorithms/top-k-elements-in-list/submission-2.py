class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # base case
        if len(nums) == 1:
            return nums

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        sorted_count = sorted(list(count.items()), key=lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_count[i][0])

        return res