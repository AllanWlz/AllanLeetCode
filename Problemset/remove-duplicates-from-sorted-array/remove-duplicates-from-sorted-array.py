
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:24:39
# @Runtime: 44 ms
# @Memory: 14.8 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        val_thresh = -99999999999999999999
        length = 0
        while head < len(nums):
            val = nums[head]
            head += 1
            if val > val_thresh:
                nums[length] = val
                length += 1
                val_thresh = val
        return length
