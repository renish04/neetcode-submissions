class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = {}
        max_count = 0

        while j < len(s):
            if s[j] not in seen:
                seen[s[j]] = j
                j+=1

            elif s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]]+1
                seen[s[j]] = j
                j+=1
            
            else:
                seen[s[j]] = j
                j+=1

            if j-i+1 > max_count:
                max_count = j-i
            
        return max_count