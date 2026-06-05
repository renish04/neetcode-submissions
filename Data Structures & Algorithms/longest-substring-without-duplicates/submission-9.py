class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxcount = 0
        count = 0
        left = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                count += 1
                if count > maxcount:
                    maxcount = count
            elif s[i] in seen and seen[s[i]] >= left :
                left = seen[s[i]]+1
                count = i - seen[s[i]]
                seen[s[i]] = i

        
        return maxcount