class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_word = min(word1, word2, key = len)

        final = []

        for i in range(len(min_word)):
            final.append(word1[i])
            final.append(word2[i])
        final.append(word1[len(min_word):])
        final.append(word2[len(min_word):])
        # if word1 == min_word:
        #     final.append(word2[len(min_word):])
        # elif word2 == min_word:
        #     final.append(word1[len(min_word):])
        
        return "".join(final)