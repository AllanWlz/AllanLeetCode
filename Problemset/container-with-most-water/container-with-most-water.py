
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:19:58
# @Runtime: 68 ms
# @Memory: 15 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        maxArea = 0
        while(left < right):
            height_left = height[left]
            height_right = height[right]
            area = min(height_right, height_left) * (right - left)
            if area > maxArea:
                maxArea = area
            if height_left > height_right:
                right = right - 1
            else:
                left = left + 1
        return maxArea
