class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        final = []
        dq = deque()

        if k == 1:
            return nums
            
        while r < len(nums)-1:
            while r < k-1:
                while dq != deque([]) and nums[dq[-1]] < nums[r]:
                    dq.pop()
                dq.append(r)
                r += 1
            final.append(nums[dq[0]])

            l += 1
            r += 1
            if l > dq[0]:
                dq.popleft()
            
            while dq != deque([]) and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
        final.append(nums[dq[0]])
        return final





         
 