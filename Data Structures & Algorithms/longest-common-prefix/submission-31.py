class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 201
        for i in range(len(strs)):
            x = len(strs[i])
            if x < min_len:
                min_len = x
            
        out_str = ""
        for k in range(min_len):
            t = strs[0][k]
            check = True
            for j in range(1, len(strs)):
                if strs[j][k] != t:
                    check = False
                    break
            
            if check == False:
                break
         
            else:
                out_str += t
            
        return out_str