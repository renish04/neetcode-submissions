class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0
        x = 0

        while p1 < (len(nums)):
            if nums[p1] == val:
                p1 += 1
                x += 1

            elif nums[p1] != val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1

        k = len(nums) - x

        return k