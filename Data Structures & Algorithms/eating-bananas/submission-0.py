class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        summ = 0
        l = 0
        r = 0
        limit = h - len(piles) - 1
        mid = 0
        x = 0

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
            
            if (l+r) % 2 != 0 :
                mid = ((l+r)//2) + 1
            else:
                mid = (l+r) // 2
            
            
            if r % mid != 0 :
                x = (r // mid) + 1
            else:
                x = r // mid


            if x == limit:
                return mid
            elif x > limit:
                l = mid + 1
            else:
                r = mid - 1
            
        return mid
        

        