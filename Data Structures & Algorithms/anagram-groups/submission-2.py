class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapi = []
        final = []

        for i in range(len(strs)):
            dicti = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in dicti:
                    dicti[strs[i][j]] = 1
                else:
                    dicti[strs[i][j]] += 1
            mapi.append(dicti)
        
        for i in range(len(mapi)):
            check = False
            temp = []
            for k in final:
                if strs[i] in k:
                    check = True
           
            if check == False:
                temp.append(strs[i])

                for j in range(i+1, len(mapi)):
                    if mapi[i] == mapi[j]:
                        temp.append(strs[j])
                
            if temp != []:
                final.append(temp)

        return final  

 