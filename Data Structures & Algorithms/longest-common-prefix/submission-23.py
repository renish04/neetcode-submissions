class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = {}
        for i in strs:
            short[i] = len(i)
        min_word = min(short, key = short.get)

        check_word = []

        for i in range(1, len(min_word)+1):
            check_word.append(min_word[0:i])
        for i in range(len(check_word)):
            for j in strs:
                if j[0] != check_word[0]:
                    return ""
                    break
                else: 
                    if j[0:i+1] == check_word[i]:
                        continue
                
                    elif j[0:i+1] != check_word[i]:
                        return check_word[i-1]