class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                sub_left = s[left + 1: right + 1]
                sub_right = s[left : right]
                return sub_left == sub_left[::-1 ] or sub_right == sub_right[::-1]
            left += 1
            right -= 1
        return True