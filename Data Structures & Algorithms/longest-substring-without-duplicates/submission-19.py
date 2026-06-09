class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        hm = {}
        maxi = 0

        while j < len(s):
            if s[j] not in hm:
                hm[s[j]] = j
                j += 1
            else:
                if hm[s[j]] < i:
                    hm[s[j]] = j
                    j += 1
                else:
                    i = hm[s[j]]+1
                    hm[s[j]] = j
                    j += 1
            
            if j - i > maxi:
                maxi = j - i
        
        return maxi