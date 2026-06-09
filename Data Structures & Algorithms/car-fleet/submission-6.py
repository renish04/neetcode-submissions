class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        hashmap = {}

        for i in range(len(position)):
            hashmap[position[i]] = speed[i]
        
        position.sort()

        if (target - position[-1]) % hashmap[position[-1]] == 0:
            factor = (target - position[-1]) // hashmap[position[-1]]
        else:
            factor = ((target - position[-1]) // hashmap[position[-1]]) + 1

        for i in range(len(position)):
            position[i] += (factor*hashmap[position[i]])
        
        fleet = 0

        while position:
            r = position.pop()
            if r <= target:
                while position and position[-1] >= r:
                    position.pop()
            elif r > target:
                while position and position[-1] >= target:
                    position.pop()               
            fleet += 1

        
        return fleet

