class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lim = min(len(word1), len(word2))
        s = []
        for i in range(lim):
            s.append(word1[i])
            s.append(word2[i])
        s.append(word1[lim:])
        s.append(word2[lim:])

        return "".join(s)