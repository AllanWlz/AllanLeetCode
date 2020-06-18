
// @Title: 整数反转 (Reverse Integer)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:16:34
// @Runtime: 0 ms
// @Memory: 6.3 MB

class Solution {
public:
    int reverse(int x) {
        long long int output = 0;
        while(x != 0)
        {
            output *= 10;
            int res = x - x / 10 * 10;
            output += res;
            x = x/10;
        }
        if(output <= -1 * pow(2,31) || output >= pow(2,31) - 1) output = 0;
        return output;
    }
};
