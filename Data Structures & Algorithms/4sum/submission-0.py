class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        for i in range(len(nums)-1):
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]

        final = []

        if len(nums) < 4:
            return []
        # print(nums)
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j>1 and nums[j] == nums[j-1]:
                    continue

                x = target - (nums[i]+nums[j])
                left = j+1
                right = len(nums)-1
                
                # print(i, j)
                while left < right:
                    if nums[left] + nums[right] == x:
                        final.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < len(nums) and nums[left] == nums[left-1]:
                            left += 1
                        while right < len(nums)-1 and nums[right] == nums[right+1]:
                            right -= 1
                        
                    elif nums[left] + nums[right] < x:
                        left += 1
                    else:
                        right -= 1
                   
        return final


