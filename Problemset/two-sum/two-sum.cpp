
// @Title: 两数之和 (Two Sum)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 19:58:59
// @Runtime: 20 ms
// @Memory: 8.2 MB

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict;
        int index = 0;
        int num,num_obj;
        for(auto iter=nums.begin();iter!=nums.end();iter++)
        {
            num = *iter;
            num_obj = target - num;
            if(dict.find(num_obj)!=dict.end())
            {
                break;
            }
            else
            {
                dict[num] = index;
            }
            index++;
        }
        return vector<int>{dict[num_obj], index};
    }
};
