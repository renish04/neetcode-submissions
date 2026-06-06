class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        max_count = 0
        seen = {}

        while j < len(s):
            if s[j] in seen:
                seen[s[j]] +=1
            else:
                seen[s[j]] = 1

            maxi = max(seen, key = seen.get)
            max_freq = seen[maxi]

            if (j-i+1) - max_freq <= k:        
                if (j-i+1) > max_count:
                    max_count = j-i+1

            else:
                seen[s[i]] -= 1
                i += 1
            
            j += 1
            
        return max_count

                

