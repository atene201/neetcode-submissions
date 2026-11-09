from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base cases
        if len(s) != len(t):
            return False

        counts = defaultdict(int)

        for letter in s:
            counts[letter] += 1

        for letter in t:
            counts[letter] -= 1
        
        for count in counts.values():
            if count > 0:
                return False
        return True

        
        