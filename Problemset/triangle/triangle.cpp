
// @Title: 三角形最小路径和 (Triangle)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:27:02
// @Runtime: 4 ms
// @Memory: 8.6 MB

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> buffer = vector<int>(n);
        buffer[0] = triangle[0][0];
        if(n == 1) return buffer[0];
        for(int i = 1; i < n; i++)
        {
            vector<int> col = triangle[i];
            for(int j = i;j>=0;j--)
            {
                int start = j - 1 > 0?j - 1: 0;
                int end = j + 1 < i?j + 1 : i;
                int m = buffer[start];
                for(int k = start; k < end; k ++)
                {
                    if(m > buffer[k]) m = buffer[k];
                }
                buffer[j] = m + col[j];
            }
        }
        int m = buffer[0];
        for(int k = 0; k < n; k ++)
        {
            if(m > buffer[k]) m = buffer[k];
        }
        return m;
    }
    
    
    int min(int a, int b){return a<b?a:b;}
    int max(int a, int b){return a>b?a:b;}
};
