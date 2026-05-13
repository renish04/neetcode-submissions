class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            x = s[i]
            if s[i] in s_map:
                s_map[x] += 1
            elif s[i] not in s_map:
                s_map[x] = 1
        for i in range(len(t)):
            y = t[i]
            if t[i] in t_map:
                t_map[y] +=1
            elif t[i] not in t_map:
                t_map[y] = 1

        if s_map == t_map:
            return True
        return False        

