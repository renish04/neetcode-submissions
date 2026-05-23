class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = []
        minword = min(strs, key = len)
        for i in range(len(minword)):
            check = True
            for j in range(len(strs)):
                if minword[i] != strs[j][i]:
                    check = False
                    return "".join(s)
            if check == True:
                s.append(minword[i])


        return "".join(s) 