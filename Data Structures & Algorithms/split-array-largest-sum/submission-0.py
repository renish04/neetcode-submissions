class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0

        for i in nums:
            if i > l:
                l = i
            
        for j in nums:
            r += j
        
        while l <= r:
            mid = (l+r) // 2

            tot = 0
            add = 0
            for i in nums:
                if add + i <= mid:
                    add += i
                else:
                    tot += 1
                    add = i
            tot += 1

            if tot <= k:
                r = mid - 1
            else:
                l = mid + 1
            
        return l