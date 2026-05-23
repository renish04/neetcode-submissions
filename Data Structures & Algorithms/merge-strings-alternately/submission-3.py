class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []

        if len(word2) > len(word1):
            for i in range(len(word1)):
                s.append(word1[i])
                s.append(word2[i])
            s.append(word2[len(word1): ])
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                s.append(word1[i])
                s.append(word2[i])
            s.append(word1[len(word2): ])
        else:
            for i in range(len(word1)):
                s.append(word1[i])
                s.append(word2[i])
        return "".join(s)