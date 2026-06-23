class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((timestamp, value))
        else:
            self.hashmap[key] = [(timestamp, value)]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            arr = self.hashmap[key]

            l = 0
            r = len(arr) - 1 

            while l <= r:
                mid = (l+r) // 2

                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                
                elif arr[mid][0] < timestamp:
                    l = mid + 1

                else:
                    r = mid - 1

        return arr[mid][1]
