class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        j = k - 1
        final = []

        if len(arr) == 1:
            return arr

        while j < len(arr)-1:
            if abs(arr[j+1]-x) < abs(arr[i]-x):
                j += 1
                i += 1
            elif abs(arr[j+1]-x) == abs(arr[i]-x):
                if arr[j+1] < arr[i]:
                    i += 1
                    j += 1
                else:
                    break
            else:
                break
                
        for m in range(i, j+1):
            final.append(arr[m])
        
        return final


        
