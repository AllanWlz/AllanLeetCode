
# @Title: 最近的请求次数 (Number of Recent Calls)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:28:23
# @Runtime: 652 ms
# @Memory: 18.4 MB

class RecentCounter:

    def __init__(self):
        self.ping_history = [ ]

    def ping(self, t: int) -> int:
        self.ping_history.append(t)
        idx = binary_search(self.ping_history, 0, len(self.ping_history), t-3000)
        self.ping_history = self.ping_history[idx:]
        return len(self.ping_history)

def binary_search(nums, l, r, t):
    while l < r:
        mid = int((l + r) / 2)
        if nums[mid] < t:
            return binary_search(nums, mid + 1, r, t)
        else:
            return binary_search(nums, l, mid, t)
    return l

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
