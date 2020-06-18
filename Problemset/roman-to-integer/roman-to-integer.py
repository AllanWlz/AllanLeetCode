
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:20:31
# @Runtime: 68 ms
# @Memory: 13.8 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':-2,'IX':-2,'XL':-20,'XC':-20,'CD':-200,'CM':-200}
        sum=0
        for k in range (len(s)-1):
            sum=sum+dict[s[k]]
            if (s[k]+s[k+1] in dict):
                sum=sum+dict[s[k]+s[k+1]]
        sum=sum+dict[s[-1]]
        return sum
