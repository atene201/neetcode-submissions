class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap to count all the letters in s
        # iterate over all the chars in t and remove each char from the hashmap from s

        if len(s) != len(t):
            return False

        s_count = {}

        for chr in range(len(s)):
            s_count[s[chr]] = s_count.get(s[chr], 0) + 1
            s_count[t[chr]] = s_count.get(t[chr], 0) - 1
        
        return all(v == 0 for v in s_count.values())

