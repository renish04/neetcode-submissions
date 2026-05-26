class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = nums[0]
        element2 = 0
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == element1:
                count1 += 1
            elif count2 == 0:
                element2 = nums[i]
                count2 +=1 
            elif nums[i] == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 == 0:
                    element1 == nums[i]
                    count1 += 1
                elif count2 == 0:
                    element2 == nums[i]
                    count2 += 1
        
        ele_1_count = 0
        ele_2_count = 0

        for i in range(len(nums)):
            if nums[i] == element1:
                ele_1_count += 1
            elif nums[i] == element2:
                ele_2_count += 1
        

        if ele_1_count > (len(nums)/3) and ele_2_count > (len(nums)/3)  :
            return [element1, element2]
        elif ele_1_count > (len(nums)/3):
            return [element1]
        elif ele_2_count > (len(nums)/3):
            return [element2]
        else:
            return []
            