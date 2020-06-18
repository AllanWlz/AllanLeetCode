
# @Title: 下一个排列 (Next Permutation)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:25:56
# @Runtime: 48 ms
# @Memory: 13.8 MB

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_value = nums[-1]
        pos = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_value:
                min_max = max_value
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i] and nums[j] < min_max:
                        min_max = nums[j]
                        pos = j
                self.inplace_swap(nums, i, pos)
                for k in range(i + 1, len(nums)):
                    pos = len(nums) - k + i
                    if k >= pos:
                        return
                    self.inplace_swap(nums, k, pos)
                return
            else:
                if nums[i] > max_value:
                    max_value = nums[i]
                    pos = i
                    
        for i in range(len(nums) - 1):
            pos = len(nums) - i - 1
            if i >= pos:
                return
            self.inplace_swap(nums, i, pos)
        
    @staticmethod
    def inplace_swap(nums, i, j):
        a = nums[i]
        nums[i] = nums[j]
        nums[j] = a
