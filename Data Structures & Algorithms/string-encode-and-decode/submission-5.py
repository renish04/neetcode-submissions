class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            x = len(strs[i])
            s += str(x) + "#"
            for j in range(x):
                s += strs[i][j]
        print(s)
        return s

    def decode(self, s: str) -> List[str]: 
        strs = []  
        m = ""
        i = 0
        while i < (len(s)):
            if s[i] == "#":
                x = int(m)
                if x == 0:
                    strs.append("")
                    m = ""
                    i += 1
                else:
                    y = s[i+1:i+1+x]
                    strs.append(y)
                    i = i+1+x
                    m = ""
            else:
                m += s[i]
                i += 1
        return strs
