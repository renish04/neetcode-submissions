class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        hashmap = {}

        for i in range(len(position)):
            hashmap[position[i]] = speed[i]
        
        position.sort()
        
        fleet = 0

        while position:
            r = position.pop()
            fleet += 1

            if (target - r) % hashmap[r] == 0:
                factor = (target - r) // hashmap[r]
            else:
                factor = ((target - r) // hashmap[r]) + 1

            r += (factor*hashmap[r])
            s = (position[-1] + factor*hashmap[position[-1]])

            while position and s >= target:
                
                if s >= r:
                    position.pop()
                    continue
                else:
                    fleet += 1
                    position.pop()
                
                s = (position[-1] + factor*hashmap[position[-1]])
        
        return fleet

