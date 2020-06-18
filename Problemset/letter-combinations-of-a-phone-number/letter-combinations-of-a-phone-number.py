
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:21:23
# @Runtime: 48 ms
# @Memory: 13.8 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        ar = []
        if '1' in digits or '0' in digits or len(digits)<=0:
            return []
        for i in (digits):
            if int(i) in d:
                ar.append(list(d[int(i)]))
    
        for i in range(len(ar)-1,0,-1):
            ans = []
            for char in ar[i-1]:
                for char2 in ar[i]:
                    ans.append(char+char2)
            ar[i-1] = ans

        return ar[0] 
