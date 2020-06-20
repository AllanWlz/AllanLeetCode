
# @Title: 寻找峰值 (Find Peak Element)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-19 17:12:15
# @Runtime: 40 ms
# @Memory: 13.8 MB

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        nums.append(-1 * sys.maxsize)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid + 1] > nums[mid]:
                l = mid
                continue
            else:
                r = mid
                continue
        return l
