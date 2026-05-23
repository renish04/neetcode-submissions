class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s= set()
        minword = min(strs, key = len)
        for i in range(len(minword)):
            for j in range(len(strs)):
                if minword[i] != strs[j][i]:
                    return "".join(s)
                else:
                    s.append(minword[i])

        return "".join(s) 