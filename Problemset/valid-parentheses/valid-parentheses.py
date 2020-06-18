
# @Title: 有效的括号 (Valid Parentheses)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:23:43
# @Runtime: 40 ms
# @Memory: 13.7 MB

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for char in s:
            if len(bracket_stack) > 0:
                if char == ')' and bracket_stack[-1] == '(' or char == '}' and bracket_stack[-1] == '{' or char == ']' and bracket_stack[-1] == '[':
                    bracket_stack.pop()
                else:
                    bracket_stack.append(char)
            else:
                bracket_stack.append(char)
        return len(bracket_stack) == 0
