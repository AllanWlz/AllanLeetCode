
# @Title: 数组的度 (Degree of an Array)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-20 18:47:13
# @Runtime: 276 ms
# @Memory: 14.9 MB

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = dict()
        start_pos = dict()
        end_pos = dict()
        for pos, x in enumerate(nums):
            if x not in degree:
                degree[x] = 1
                start_pos[x] = pos
                end_pos[x] = pos
            else:
                degree[x] += 1
                end_pos[x] = pos
        
        largest_degree = 0
        best_key_range = len(nums)
        best_key = 0
        for key in degree:
            if degree[key] > largest_degree:
                largest_degree = degree[key]
                best_key = key
                best_key_range = end_pos[key] - start_pos[key] + 1
            elif degree[key] == largest_degree:
                key_range = end_pos[key] - start_pos[key] + 1
                if key_range < best_key_range:
                    best_key = x
                    best_key_range = key_range
        return best_key_range
