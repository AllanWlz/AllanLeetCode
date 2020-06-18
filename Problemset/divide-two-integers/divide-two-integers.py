
# @Title: 两数相除 (Divide Two Integers)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:25:34
# @Runtime: 40 ms
# @Memory: 13.7 MB

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend >= 0) is (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        i, tmp = 1, divisor
        while dividend >= divisor:
            if dividend < (tmp << 1):
                res += i
                dividend = dividend - tmp
                i, tmp = 1, divisor
                continue
            i = i << 1
            tmp = tmp << 1
        if not positive:
            res = res - res - res
        if res < -2147483648 or res > 2147483647:
            res = 2147483647
        return res
