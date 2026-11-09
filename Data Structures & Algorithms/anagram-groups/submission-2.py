class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # base cases
        if len(strs) == 0:
            return [[]]
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    

        