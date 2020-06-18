
# @Title: 数位成本和为目标值的最大数字 (Form Largest Integer With Digits That Add up to Target)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:28:43
# @Runtime: 372 ms
# @Memory: 25.8 MB

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        num_len = len(cost)
        dp = [[''] * (target + 1)] * (num_len + 1)
        
        for i in range(1, num_len + 1):
            for j in range(1, target + 1):
                a = cost[i - 1]
                if j - a < 0:
                    s2 = ''
                elif j - a == 0:
                    s2 = str(i)
                else:
                    s2 = dp[i][j - a]
                    if s2 == '':
                        continue
                    s2 = str(i) + s2
                    
                s1 = dp[i-1][j]
                if self.string_greater_than(s1, s2):
                    dp[i][j] = s1
                else:
                    dp[i][j] = s2

        if dp[num_len][target] == '':
            return '0'
        return dp[num_len][target]
                    
    def string_greater_than(self, s1, s2):
        if len(s1) != len(s2):
            return len(s1) > len(s2)
        else:
            return s1 > s2
