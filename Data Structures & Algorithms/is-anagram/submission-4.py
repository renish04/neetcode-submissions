class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in s_hash:
                    s_hash[s[i]] = 1
                elif s[i] in s_hash:
                    s_hash[s[i]] += 1
                if t[i] not in t_hash:
                    t_hash[t[i]] = 1
                elif t[i] in t_hash:
                    t_hash[t[i]] += 1
        if t_hash == s_hash:
            return True
        return False