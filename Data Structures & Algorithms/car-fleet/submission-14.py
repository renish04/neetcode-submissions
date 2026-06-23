class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}

        for i in range(len(position)):
            time[position[i]] = (target - position[i]) / speed[i]

        position.sort()

        fleet = -1

        for i in range(len(position)):
            while position:    
                r = position.pop()
                t = time[r]

            while position and time[position[-1]] <= t:
                position.pop()
                continue
            fleet += 1

        return fleet
