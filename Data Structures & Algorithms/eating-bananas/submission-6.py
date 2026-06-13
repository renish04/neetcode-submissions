class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = 0
        mini = 0

        for i in piles:
            mini += i
        
        if mini % h != 0:
            l = (mini // h) + 1
        else:
            l = mini // h

        for j in piles:
            if j > r:
                r = j
            
        while l <= r:
            mid = (l+r) // 2

            tot = 0
            for i in piles:
                if i < mid:
                    tot += 1
                elif i % mid !=0 :
                    tot += (i // mid) + 1
                else:
                    tot += (i // mid)
                
            if tot <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l