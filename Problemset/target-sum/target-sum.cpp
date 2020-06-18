
// @Title: 目标和 (Target Sum)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:27:54
// @Runtime: 776 ms
// @Memory: 47.6 MB

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        unordered_map<int, unordered_map<int, int>>dp_map;
        dp_map[0][-nums[0]] = 1;
        dp_map[0][nums[0]] = (dp_map[0][nums[0]]?2:1);
        for(int i=1;i<nums.size();i++)
        {
            for(auto it:dp_map[i-1])
            {
                dp_map[i][it.first + nums[i]]+=dp_map[i-1][it.first];
                dp_map[i][it.first - nums[i]]+=dp_map[i-1][it.first];
            }
        }
        return dp_map[nums.size()-1][S];
    }
};
