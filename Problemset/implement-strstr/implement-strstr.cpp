
// @Title: 实现 strStr() (Implement strStr())
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:25:07
// @Runtime: 8 ms
// @Memory: 7.2 MB

class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = needle.size(), j = 0;
        if(m == 0) return 0;
        int n = haystack.size(), i = 0;
        int* next = buildNext(needle);
        while(j < m && i < n)
        {
            if(j < 0 || haystack[i] == needle[j])
            {
                i++; j++;
            }
            else
            {
                j = next[j];
            }
        }
        delete [] next;
        if(j != m) return -1;
        return i - j;
    }
    
    int* buildNext(string p)
    {
        int m = p.size();
        int* next = new int[m];
        int t = next[0] = -1;
        int j = 0;
        while(j < m - 1)
        {
            if(t < 0 || p[j] == p[t])
            {
                j++; t++;
                next[j] = (p[j] != p[t]?t:next[t]);
            }
            else t = next[t];
        }
        return next;
    }
};


