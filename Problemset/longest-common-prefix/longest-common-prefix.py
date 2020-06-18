
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:20:39
# @Runtime: 52 ms
# @Memory: 13.5 MB

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        if len(strs) == 0:
            return ""
        if len(strs[0]) == 0:
            return ""
        while True:
            if len(strs[0]) < index + 1:
                break
            character = strs[0][index]
            align_symbol = True 
            for string in strs:
                if len(string) < index + 1 or string[index] != character:
                    align_symbol = False
                    break
            if not align_symbol:
                break
            index = index + 1
        return strs[0][:index]
