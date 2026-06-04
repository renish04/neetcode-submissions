class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        score = 0

        left = 0
        right = len(people) - 1

        while left <= right:
            if left == right:
                score += 1
                return score

            # if people[right] == limit:
            #     score += 1
            #     right -= 1
            if people[right] > limit:
                right -= 1
            
            elif people[left] + people[right] <= limit:
                score += 1
                left += 1
                right -= 1
            else:
                score += 1
                right -= 1

        return score

