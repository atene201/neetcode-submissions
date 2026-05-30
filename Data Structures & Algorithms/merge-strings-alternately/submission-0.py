class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        res = ""
        w1 = len(word1)
        w2 = len(word2)

        if w1 < w2:
            j = w1
        else:
            j = w2

        while i < j:
            res += word1[i]
            res += word2[i]
            i +=1

        while i < w1:
            res += word1[i]
            i +=1

        while i < w2:
            res += word2[i]
            i +=1
            
        return res
