class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()

        left = 0
        result = 0
        for right in range(len(s)):
            # abcdde
            # pwwkew
            # p charSet = p
            # w charSet = pw
            # w charSet = p
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            result = max(result, (right - left) + 1)
            charSet.add(s[right])
        return result

        
        


        