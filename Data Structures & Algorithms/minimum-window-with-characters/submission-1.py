class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}
        posn = {}
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
                    posn[s[i]] = i
                elif hash_s[s[i]] < hash_t[s[i]] :
                    hash_s[s[i]] += 1
                elif hash_s[s[i]] == hash_t[s[i]]:
                    posn[s[i]] = i
            if hash_t == hash_s:
                # maxi = max(posn, key = posn.get)
                # max_dis = posn[maxi]
                mini = min(posn, key = posn.get)
                min_dis = posn[mini]

                if i - min_dis < min_count:
                    min_count = i - min_dis + 1
                    min_str = s[min_dis : i+1]

        return min_str



             
        
