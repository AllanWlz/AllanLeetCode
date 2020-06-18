
# @Title: 字符串转换整数 (atoi) (String to Integer (atoi))
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:17:59
# @Runtime: 48 ms
# @Memory: 13.7 MB

class Solution:
    def myAtoi(self, str: str) -> int:
        ls = str.strip()
        if len(ls) == 0:
            return 0
        acceptedVal = '+-0123456789'
        if ls[0] not in acceptedVal:
            return 0
        
        sign = 1
        atoiVal = 0
        i = 0
        
        if ls[0] == '-':
            sign = -1
            i = 1
        elif ls[0] == '+':
            i = 1
        
        while(i < len(ls) and ls[i].isdigit()):
            atoiVal = atoiVal * 10 + (ord(ls[i]) - ord('0'))
            i += 1
        return max(-2**31, min(sign * atoiVal, 2**31 - 1))        
