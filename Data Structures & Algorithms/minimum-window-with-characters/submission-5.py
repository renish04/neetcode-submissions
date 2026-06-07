class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}
        have = 0
        min_count = float('inf')
        min_str = ""

        for i in range(len(t)):
            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1

        need = len(hash_t)  # CHANGE 1: moved here, distinct chars not len(t)
                
        left = 0
        right = 0

        while right < len(s):
            if s[right] in hash_t: 
                if s[right] in hash_s:
                    hash_s[s[right]] += 1
                else:
                    hash_s[s[right]] = 1
                if hash_s[s[right]] == hash_t[s[right]]:  # CHANGE 2: only increment have when quota exactly met
                    have += 1
                right += 1

                while have == need:  # CHANGE 3: was if/elif, now a while that captures AND contracts
                    if right - left < min_count:
                        min_count = right - left
                        min_str = s[left : right]
                    if s[left] in hash_t:
                        if hash_s[s[left]] == hash_t[s[left]]:
                            have -= 1
                        hash_s[s[left]] -= 1
                    left += 1
                    
            else:
                right += 1
            
        return min_str