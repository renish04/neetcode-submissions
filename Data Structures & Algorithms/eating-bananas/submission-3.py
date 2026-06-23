class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        summ = 0
        l = 0
        r = 0

        for i in piles:
            summ += i

        if summ % h != 0 :
            l = (summ // h) + 1
        else:
            l = summ // h
        
        for i in piles:
            if i > r:
                r = i
        
        while l <= r:
            mid = 0
            if (l+r) // 2 != 0 :
                mid = ((l+r)//2) + 1
            else:
                mid = (l+r) // 2
            
            tot = 0
            for i in piles:
                if i % mid != 0:
                    tot += (i // mid) + 1
                else:
                    tot += i // mid
            
            if tot <= h:
                r = mid - 1
            elif tot > h :
                l = mid + 1

        return mid
        

        