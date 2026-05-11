class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        
        # abcde
        # abaede

        # if the next char is the same as the old one we move the starting point one right
        # if the next char is already in the substring

        for right in range(len(s)):
            start = ""
            check = set()

            copy_start = right
            while copy_start < len(s):
                if s[copy_start] not in check:
                    check.add(s[copy_start])
                    start += s[copy_start]
                    if len(start) > len(longest):
                        longest = start
                        print(longest)
                    copy_start += 1
                else:
                    break
        return len(longest)

                



            