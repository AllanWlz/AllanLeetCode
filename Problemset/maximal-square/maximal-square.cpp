
// @Title: 最大正方形 (Maximal Square)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:27:28
// @Runtime: 88 ms
// @Memory: 14.1 MB

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int maxlen = 0;
        int n = matrix.size();
        if(n==0) return 0;
        int m = matrix[0].size();
        if(m==0) return 0;
        list<pair<int, int>> base_list;
        for(int i = 0;i<n;i++)
        {
            for(int j = 0;j<m;j++)
            {
                base_list.push_back(pair<int, int>(i, j));
            }
        }
        while(true)
        {
            for(auto iter = base_list.begin(); iter != base_list.end();)
            {
                //cout<<iter->first<<iter->second<<endl;
                int t = expandSquare(matrix, *iter, maxlen, n, m);
                if(t <= maxlen)
                {
                    base_list.erase(iter++);
                }
                else
                {
                    iter++;
                }
            }
            if(base_list.empty())
            {
                break;
            }
            else
            {
                maxlen += 1;
            }
        }
        return maxlen * maxlen;
    }
    
    int expandSquare(vector<vector<char>>& matrix, pair<int, int> pos, int maxlen, int n, int m)
    {
        if(pos.first + maxlen > n - 1 || pos.second + maxlen > m - 1) return maxlen;
        for(int i = pos.first; i < pos.first + maxlen + 1; i ++ )
        {
            if(matrix[i][pos.second + maxlen] != '1') return maxlen;
        }
        for(int j = pos.second; j < pos.second + maxlen + 1; j ++ )
        {
            if(matrix[pos.first + maxlen][j] != '1') return maxlen;
        } 
        return maxlen + 1;
    }
};
