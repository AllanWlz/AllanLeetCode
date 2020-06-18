
// @Title: 正则表达式匹配 (Regular Expression Matching)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:19:27
// @Runtime: 4 ms
// @Memory: 6.2 MB

static int lambda0 = [](){
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	return 0;
}();

class Solution {
public:
    bool isMatch(string s, string p)
    {
        int dp[(s.size() + 1)*(p.size() + 1)];
        for(int i=0;i < (s.size() + 1)*(p.size() + 1);i++) dp[i]=0;
        dp[(s.size() + 1)*(p.size() + 1)-1] = 1;
        for(int i = s.size();i>=0;i--){
            for(int j = p.size() - 1;j>=0;j--)
            {
                bool first_match = i < s.size() and (s[i] == p[j] or p[j] == '.');
                if(p[j + 1] == '*')
                {
                    dp[j + i * (p.size() + 1)] = dp[j + 2 + i * (p.size() + 1)] or (first_match and dp[j + (i + 1) * (p.size() + 1)]);
                }
                else
                {
                    dp[j + i * (p.size() + 1)] = (first_match and dp[j + 1 + (i + 1) * (p.size() + 1)]);
                }
            }
        }
        return dp[0];
    }
};
