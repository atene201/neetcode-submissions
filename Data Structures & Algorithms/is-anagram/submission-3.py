class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap to count all the letters in s
        # iterate over all the chars in t and remove each char from the hashmap from s

        s_count = {}

        for chr in s:
            s_count[chr] = s_count.get(chr,0) + 1

        for chr in t:
            if chr not in s_count.keys():
                return False
            if s_count[chr] == 0:
                s_count[chr] += 1
            s_count[chr] -= 1
        
        print(sum(s_count.values()))
        if sum(s_count.values()) == 0:
            return True
        else:
            return False

