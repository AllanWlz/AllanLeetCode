
# @Title: 三数之和 (3Sum)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:20:47
# @Runtime: 2080 ms
# @Memory: 18 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count_set = {}
        for num in nums:
            if num in count_set:
                count_set[num] = count_set[num] + 1 if count_set[num] < 3 else 3
            else:
                count_set[num] = 1
        pos = 0
        new_nums = nums
        for num in count_set:
            for i in range(count_set[num]):
                new_nums[pos + i] = num
            pos = pos + count_set[num]
        new_nums = new_nums[:pos]
        
        solution_set = []
        flag_set = {}
        for i in range(len(new_nums)):
            two_sum = 0 - new_nums[i];
            sum_dict = {}
            for j in range(len(new_nums)):
                if i == j:
                    continue
                one_sum = two_sum - new_nums[j]
                if one_sum in sum_dict:
                    solution = [new_nums[i], new_nums[j], one_sum]
                    solution.sort()
                    string = tuple(solution)
                    if string not in flag_set:
                        solution_set.append(solution)
                        flag_set[string] = 1
                else:
                    sum_dict[new_nums[j]] = 1
        return solution_set
                
