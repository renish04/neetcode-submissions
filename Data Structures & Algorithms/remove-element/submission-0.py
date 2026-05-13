class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = len(nums)
        i = 0
        while(i < x):
            if nums[i] == val:
                nums.remove(nums[i])
                x = len(nums)
                continue
            else:
                i +=1
        k = len(nums)

        return k