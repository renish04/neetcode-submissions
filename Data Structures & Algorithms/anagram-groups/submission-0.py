class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapi = []
        final = []
        for i in range(len(strs)):
            andict = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in andict:
                    andict[strs[i][j]] = 1
                else:
                    andict[strs[i][j]] += 1
            mapi.append(andict)

        for i in range(len(mapi)):
            temp = []
            x = False
            for sublist in range(len(final)):     
                if strs[i] in final[sublist]:
                    x = True
        
            if x == True:
                continue
            if x == False:
                temp.append(strs[i])
            
            for j in range(i+1, len(mapi)):
                if mapi[j] == mapi[i]:
                    temp.append(strs[j])

            final.append(temp)
        
        return final


         