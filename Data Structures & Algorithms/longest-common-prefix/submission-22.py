class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortword = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(shortword):
                shortword = strs[i]
            if strs[i]  == "":
                return ""
        
        for i in range(len(shortword)):
            x = shortword[0:i+1]
            for j in range(len(strs)):
                if shortword[0] != strs[j][0]:
                    return ""
                if x == strs[j][0:i+1]:
                    pass
                elif x != strs[j][0:i+1]:
                    print(f"exectuted for x : {x}")
                    return shortword[0:i]
        return shortword            
                