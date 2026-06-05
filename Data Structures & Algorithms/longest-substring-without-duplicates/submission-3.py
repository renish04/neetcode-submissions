class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        seen = set()
        
        maxsub = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                sub += s[i]
                if len(sub) > maxsub:
                    maxsub = len(sub)
            else:
                # if len(sub) > maxsub:
                #     maxsub = len(sub)
                j = 0
                while sub[j] != s[i]:
                    seen.remove(sub[j])
                    j += 1
                seen.remove(s[i])
                sub = sub[j+1:] + s[i]
                seen.add(s[i])
            
        return maxsub