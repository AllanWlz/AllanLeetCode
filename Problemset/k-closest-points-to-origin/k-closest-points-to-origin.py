
# @Title: 最接近原点的 K 个点 (K Closest Points to Origin)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-19 16:34:27
# @Runtime: 908 ms
# @Memory: 19.1 MB

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:K]
