class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0
        x = 0
        for a in range(len(nums)):
            if nums[a] == val:
                x += 1
                a += 1
            
            elif nums[a] != val:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1

    

        k = len(nums) - x
        return k
            