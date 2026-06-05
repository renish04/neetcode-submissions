class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win_len = 0
        max_len = 1
        hashmap = {}
        left = 0
        i = 0

        while i < len(s) and left <= i:
            win_len = i - left + 1
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
            maxi = max(hashmap, key = hashmap.get)
            max_freq = hashmap[maxi]

            
            if win_len - max_freq <= k:
                if win_len > max_len:
                    max_len = win_len

            while win_len - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1
                win_len -= 1
                maxi = max(hashmap, key = hashmap.get)
                max_freq = hashmap[maxi]
            i += 1

        return max_len


