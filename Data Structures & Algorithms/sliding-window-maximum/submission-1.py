class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        m = 0
        final = []

        while r < len(nums) - 1:
            while r - l + 1 < k:
                r += 1
                if nums[r] > nums[m]:
                    m = r
            if r == len(nums)-1:
                break
            final.append(nums[m])
            
            l += 1
            r += 1

            if nums[r] >= nums[m]:
                m = r
            elif nums[r] < nums[m] and m >= l:
                continue
            else:
                m = l
                for i in range(l, r+1):
                    if nums[i] > nums[m]:
                        m = i

        final.append(nums[m])
        return final





         
 