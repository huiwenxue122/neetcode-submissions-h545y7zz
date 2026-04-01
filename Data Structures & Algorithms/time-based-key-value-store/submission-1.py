class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        # 直接加进去就行，因为时间是递增的，不需要排序。
    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, []) #先拿到这个 key 的所有记录 如果没有这个 key，就返回空列表

        # 然后二分找：最后一个 timestamp <= 给定 timestamp
        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
