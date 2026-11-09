class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # base cases
        if len(s) == 1:
            return True

        # whitespaces should be removed before comparing
        # all letters should be lowercase
        # edge case: ? ! still allow for a valid palindrome

        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()

        return res == res[::-1]

        