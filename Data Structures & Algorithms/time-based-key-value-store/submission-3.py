class TimeMap:

    def __init__(self):
        self.storeKey = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storeKey:
            self.storeKey[key] = []
        self.storeKey[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.storeKey.get(key, [])
        l, r = 0, len(values) -1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result