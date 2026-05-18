class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        s = "f.a.a".join(strs)

        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        if s == "":
            strs.append(s)
            return strs 
        m = ""
        i = 0

        while i < len(s):

            if s[i] == "f" and (len(s) - (i+1) >= 5):
                if s[i:i+5] == "f.a.a":
                    strs.append(m)
                    m = ""
                    i = i+5

            elif i == len(s) - 1:
                    m += s[i]
                    strs.append(m)
                    m = ""
                    i += 1    
            else:
                m += s[i]
                i += 1
        return strs