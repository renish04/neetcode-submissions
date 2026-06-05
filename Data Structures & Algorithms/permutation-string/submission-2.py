class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = {}
        hash2 = {}
        i = 0
        j = len(s1) - 1

        if len(s2) < len(s1):
            return False

        for k in range(len(s1)):
            if s1[k] in hash1:
                hash1[s1[k]] += 1
            else:
                hash1[s1[k]] = 1
            if s2[k] in hash2:
                hash2[s2[k]] += 1
            else:
                hash2[s2[k]] = 1
        
        while j < len(s2):
          
            if hash2 == hash1:
                return True
            else:
                hash2[s2[i]] -= 1
                if hash2[s2[i]] == 0:
                    hash2.pop((s2[i]))
                if j+1 < len(s2):
                    if s2[j+1] in hash2:
                        hash2[s2[j+1]] += 1
                    else:
                        hash2[s2[j+1]] = 1
                
            i += 1
            j += 1
        
        return False

