
// @Title: Z 字形变换 (ZigZag Conversion)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:16:24
// @Runtime: 16 ms
// @Memory: 8.1 MB

int fast_io=[](){ios_base::sync_with_stdio(false);cin.tie(NULL);return 0;}();
class Solution {
public:
    string convert(string s, int numRows) {
        string output("");
        if(numRows==1) return s;
        int row_step = 2 * numRows - 2;
        for(int row = 0;row < numRows;row++)
        {
            int pos = row;
            int first_step = row_step - 2 * (row % (numRows - 1));
            int second_step = row_step - first_step;
            int step = 1;
            if(second_step==0) second_step=first_step;
            while(pos<s.size())
            {
                output.append(1, s[pos]);
                if(step % 2) pos += first_step;
                else pos += second_step;
                step++;
            }
        }
        return output;
    }
};
