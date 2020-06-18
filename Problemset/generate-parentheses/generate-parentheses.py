
# @Title: 括号生成 (Generate Parentheses)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:24:00
# @Runtime: 40 ms
# @Memory: 13.8 MB

class Solution:
    def helper(self, n,ans,string,l,r):
        if len(string) == n*2:
            ans.append(string)
            return
        if l < n:
            self.helper(n,ans,string+'(',l+1,r)
        if r < l:
            self.helper(n,ans,string+')',l,r+1)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        string = ""
        self.helper(n,ans,string,0,0)
        return ans
