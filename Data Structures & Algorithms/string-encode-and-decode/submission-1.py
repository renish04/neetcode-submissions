class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            if strs[i] == "":
                s += "_"
                continue

            for j in range(len(strs[i])):
                if j == 0:
                    s += "#"

                x = ord(strs[i][j])
                x += 1
                y = chr(x)
                s += y
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        m = ""
        for i in range(len(s)):
            
            if i == 0 and s[0] == "#":
                continue
            if s[i] ==  "_":
                
                strs.append(m)
                continue
                
            elif s[i] != "#":
                
                x = ord(s[i])
                x -= 1
                y = chr(x)
                m += y

            elif s[i] == "#" and i != 0:
                
                strs.append(m)
                m = ""
            if i == (len(s)-1):
                strs.append(m)
        return strs


        