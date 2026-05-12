class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for _ in range(len(nums) + 1)] # +1 because range is exclusive

        for num in nums:
            count[num] = count.get(num, 0) + 1

        
        for num, count in count.items():
            # assign the index corresponding to the value of count and append the num
            freq[count].append(num)

        res = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        




