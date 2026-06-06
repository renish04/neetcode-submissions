class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        i = 0
        j = k-1

        if len(arr) == k:
            return arr
        
        while j < len(arr):
            close = abs(x-arr[i])
            if j < len(arr)-1 and abs(arr[j+1]-x) < close:
                i += 1
                j += 1
            elif j < len(arr)-1 and abs(arr[j+1]-x) == close:
                if arr[j+1] <= arr[i]:
                    i += 1
                    j += 1
                else: 
                    for m in range(i, j+1):
                        ans.append(arr[m])
                    break
            # else:
            #     for m in range(i, j+1):
            #         ans.append(arr[m])
            #     break
        return ans 



