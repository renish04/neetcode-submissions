class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = nums[0]
        count1 = 0
        element2 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == element1:
                count1 += 1
            elif nums[i] == element2:
                count2 += 1

            elif count1 == 0:
                element1 = nums[i]
                count1 = 1
            elif count2 == 0:
                element2 = nums[i]
                count2 = 1 
            else:
                count1 -= 1
                count2 -= 1

        print(f"ele1 - {element1}, count1 - {count1}, ele2 - {element2}, count2 - {count2}")
        total_count_1 = 0
        total_count_2 = 0

        for i in range(len(nums)):
            if nums[i] == element1:
                total_count_1 += 1
            elif nums[i] == element2:
                total_count_2 += 1
            else:
                continue

        n = (len(nums)/3)

        print("n", n)
        print(f"element1 {element1}, totalcount1 {total_count_1}")
        print(f"element2 {element2}, totalcount2 {total_count_2}")
        if total_count_1 > n and total_count_2 > n:
            return [element1, element2]
        elif total_count_1 > n and total_count_2 <= n:
            return [element1]
        elif total_count_2 > n and total_count_1 <= n:
            return [element2]
        else:
            return []