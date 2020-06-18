
# @Title: 四数之和 (4Sum)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:23:17
# @Runtime: 152 ms
# @Memory: 12.8 MB

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        solution_list = {}
        if l < 4:
            return []
        for i in range(l-3):
            if nums[i] + nums[l-3] + nums[l-2] + nums[l-1] < target:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            for j in range(i+1, l-2):
                k = j + 1
                t = l - 1
                while k < t:
                    if nums[i] + nums[j] + nums[k] + nums[t] < target:
                        k = k + 1
                    elif nums[i] + nums[j] + nums[k] + nums[t] > target:
                        t = t - 1
                    else:
                        solution_list[(nums[i], nums[j], nums[k], nums[t])] = 1
                        k = k + 1
        solution_list = solution_list.keys()         
        return solution_list
