class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final = []

        if len(nums) < 4:
            return []

        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(len(nums)-1, i, -1):
                if j<len(nums)-1 and j>=0 and nums[j] == nums[j+1]:
                    continue
                
                left = i+1
                right = j-1
                x = nums[i] + nums[j]

                while left < right:
                    if nums[left] + nums[right] == target - x:
                        final.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < len(nums)-1 and nums[left] == nums[left-1]:
                            left += 1
                        while right < len(nums)-2 and right >=0 and nums[right] == nums[right+1]:
                            right -= 1
                        
                    elif nums[left] + nums[right] < target - x:
                        left += 1
                    else:
                        right -= 1

        return final
