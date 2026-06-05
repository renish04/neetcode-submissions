class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                sub += s[i]
            else:
                j = 0
                while sub[j] != s[i]:
                    seen.pop(sub[j])
                    j += 1
                seen.pop(s[i])
                sub = sub[j+2:]
            
        return len(sub)