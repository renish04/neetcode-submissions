class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        right = n-1
        left = 0


        while left < right:
            while nums[right] == val:
                right -= 1
                if right == 0:
                    return []
                    break

            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                left += 1
        print(nums)
        k = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                k += 1
            else:
                break
        
        return n-k
            