class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        hashset = set()
        map_list = []

        for i in range(len(strs)):
            temp_hash = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in temp_hash:
                    temp_hash[strs[i][j]] = 1
                else:
                    temp_hash[strs[i][j]] += 1
            map_list.append(temp_hash)

        for i in range(len(map_list)):
            if strs[i] not in hashset:
                temp = []
                temp.append(strs[i])
                hashset.add(strs[i])
                for j in range(i+1, len(map_list)):
                    if map_list[i] == map_list[j]:
                        temp.append(strs[j])
                        hashset.add(strs[j])

                final.append(temp)
        
        return final