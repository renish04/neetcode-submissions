class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 0
        r = 0

        for i in weights:
            r += i
        
        for j in weights:
            if j > l:
                l = j
      
        while l <= r:
            mid = (l+r) // 2

            tot = 0
            add = 0

            for i in weights:
                if add+i <= mid:
                    add += i
                else:
                    tot += 1
                    add = i
                
            tot += 1
            
            if tot > days:
                l = mid + 1
            elif tot <= days:
                r = mid - 1
        
        return l