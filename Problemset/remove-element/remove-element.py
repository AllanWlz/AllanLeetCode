
# @Title: 移除元素 (Remove Element)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:24:47
# @Runtime: 64 ms
# @Memory: 13.6 MB

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] != val:
                nums[length] = nums[idx]
                length += 1
            idx += 1
        return length
