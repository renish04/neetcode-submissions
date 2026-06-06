class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        hash1 = {}
        hash2 = {}

        for i in range(len(s1)):
            if s1[i] in hash1:
                hash1[s1[i]] += 1
            else:
                hash1[s1[i]] = 1
            if s2[i] in hash2:
                hash2[s2[i]] += 1
            else:
                hash2[s2[i]] = 1
        
        left = 0
        right = len(s1)-1

        while right < len(s2):

            if hash1 == hash2:
                return True
            else:
                hash2[s2[left]] -= 1
                if hash2[s2[left]] == 0:
                    hash2.pop(s2[left])
                left += 1
                right += 1
                if right < len(s2):
                    if s2[right] in hash2:
                        hash2[s2[right]] += 1
                    else:
                        hash2[s2[right]] = 1
        return False
