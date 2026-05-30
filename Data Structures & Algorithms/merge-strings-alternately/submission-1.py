class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        res = []
        w1 = len(word1)
        w2 = len(word2)
        j = min(w1, w2)

        while i < j:
            res.append(word1[i])
            res.append(word2[i])
            i +=1

        while i < w1:
            res.append(word1[i])
            i +=1

        while i < w2:
            res.append(word2[i])
            i +=1

        return "".join(res)
