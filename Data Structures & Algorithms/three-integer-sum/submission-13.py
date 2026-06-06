class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for i in range(len(nums)-1):
        #     min = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[min]:
        #             min = j

        #     nums[i], nums[min] = nums[min], nums[i]
        nums.sort()

        final = []

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                x = nums[left] + nums[right]
                if x == -(nums[i]):
                    final.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while  left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                    while right <= len(nums)-2 and right >=0 and nums[right] == nums[right+1]:
                        right -= 1
                elif x < -(nums[i]):
                    left += 1
                elif x > -(nums[i]):
                    right -= 1
        

        return final

