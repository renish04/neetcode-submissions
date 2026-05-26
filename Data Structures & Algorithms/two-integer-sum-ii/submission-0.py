class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[j] > target - numbers[i]:
                j -= 1
            elif numbers[j] > target - numbers[i]:
                i += 1
            elif numbers[j] == target - numbers[i]:
                return [numbers[i], numbers[j]]
