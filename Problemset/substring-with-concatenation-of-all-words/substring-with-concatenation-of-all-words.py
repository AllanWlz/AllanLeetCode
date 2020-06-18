
# @Title: 串联所有单词的子串 (Substring with Concatenation of All Words)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:25:44
# @Runtime: 1428 ms
# @Memory: 14 MB

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 14:13
        if len(words) == 0:
            return []
        ret_list = []
        length = len(words[0])
        list_contain_w = dict()
        for x in words:
            self.add_word(x, list_contain_w)
        for pos in range(len(s) - len(words) * length + 1):
            s_contain_w = dict()
            for idx in range(len(words)):
                s_word = s[pos + length*idx:pos + length*(idx+1)]
                self.add_word(s_word, s_contain_w)
            flag = True
            for x in list_contain_w:
                if s_contain_w.get(x, 0) != list_contain_w[x]:
                    flag = False
                    break
            if flag:
                ret_list.append(pos)
        return ret_list
    
    
    def add_word(self, w, w_dict):
            if w in w_dict:
                w_dict[w] += 1
            else:
                w_dict[w] = 1
