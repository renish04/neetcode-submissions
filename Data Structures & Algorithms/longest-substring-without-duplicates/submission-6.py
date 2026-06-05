class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        seen = {}
        maxsub = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                sub += s[i]
                if len(sub) > maxsub:
                    maxsub = len(sub)
                print(seen)
            else:
                sub = s[seen[s[i]]+1 : i+1]
                seen[s[i]] = i
        
        return maxsub