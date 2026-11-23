class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # optimal solution would be to find the one distinct char
        # with the most appearances
        # AAABABB -> A: 4 B:3, k=1
        # return 5 because we already know A has the most so we'd just add one
        
        count = {}
        result = 0
        maxFreq = 0
        left = 0

        # ABAA
        # A, A: 1
            # maxFreq: 1
                # 0 - 0 + 1 - 1 > 0
        # B, B: 1
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq = max(maxFreq, count[s[right]])

            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result




            

        

        