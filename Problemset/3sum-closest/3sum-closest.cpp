
// @Title: 最接近的三数之和 (3Sum Closest)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:21:12
// @Runtime: 16 ms
// @Memory: 10.1 MB

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];
        for(int i = 0;i<nums.size()-2;i++)
        {
            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right)
            {
                int t = nums[i] + nums[left] + nums[right];
                res = abs(res - target) < abs(t - target)?res:t;
                if(t < target) left++;
                else right--;
            }
        }
        return res;
    }
};
