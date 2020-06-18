
// @Title: 最长回文子串 (Longest Palindromic Substring)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:16:15
// @Runtime: 4 ms
// @Memory: 6.6 MB

static const auto io_sync_off = []()
{
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    std::cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    string longestPalindrome(string s)
    {
        int len = s.size();
        int start = 0;
        int left,right;
        int maxlen = 0;
        int maxleft = 0;
        while(len - start > maxlen / 2)
        {
            left = right = start;
            while(right < len - 1 && s[right+1]==s[left]) right++;
            if(s[right+1]==s[left]) right++;
            start = right + 1;
            while(left > 0 && right < len - 1 && s[left-1]==s[right+1])
            {
                left--;
                right++;
            }
            if(right-left+1>maxlen)
            {
                maxlen = right - left + 1;
                maxleft = left;
            }
        }
        return s.substr(maxleft, maxlen);
    }
};
