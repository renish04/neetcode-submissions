class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}
        posn = [0]*len(s)
        min_count = len(s)
        min_str = ""

        for i in range(len(t)):
            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1

        for i in range(len(s)):
            if s[i] in hash_t:
                if s[i] not in hash_s:
                    hash_s[s[i]] = 1
                    posn[i] = s[i]
                elif hash_s[s[i]] < hash_t[s[i]] :
                    hash_s[s[i]] += 1
                    posn[i] = s[i]
                elif hash_s[s[i]] == hash_t[s[i]]:
                    posn[i] = s[i]
                    for m in range(len(posn)):
                        if posn[m] == s[i]:
                            posn[m] = 0
                            break
                    
            if hash_t == hash_s:
                l = 0
                r = len(s)-1
                while l < len(posn):
                    if posn[l] != 0:
                        break
                    else:
                        l += 1
                while r > -1:
                    if posn[r] != 0:
                        break
                    else:
                        r -= 1
                
                if r-l+1 < min_count:
                    min_count = r-l+1
                    min_str = s[l:r+1]


        return min_str



             
        
