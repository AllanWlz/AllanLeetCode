
// @Title: 回文数 (Palindrome Number)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:19:15
// @Runtime: 8 ms
// @Memory: 6.1 MB

static int lambda0 = []() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	return 0;
}();
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        int begin = x;
        long long int end = 0;
        while(x)
        {
            end = end * 10 + x % 10;
            x /= 10;
        }
        return begin==end;
    }
};
