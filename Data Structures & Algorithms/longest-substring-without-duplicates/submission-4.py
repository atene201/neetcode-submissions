class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers

        mp = {}
        left = 0
        right = len(s)-1
        res = 0
        for right in range(len(s)):
            # check if the character has already been seen
            if s[right] in mp:
                # jump to the index that allows for new comparison w/o repeating chars
                left = max(mp[s[right]] + 1, left)
            mp[s[right]] = right
            res = max(right - left + 1, res)
        return res
        


        