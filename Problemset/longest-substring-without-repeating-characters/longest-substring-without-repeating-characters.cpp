
// @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:15:32
// @Runtime: 52 ms
// @Memory: 11.3 MB

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
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> char_map;
        int current_length = 0;
        int max_length = 0;
        int start_index = 0;
        int index=0;
        for(auto iter=s.begin();iter!=s.end();iter++)
        {
            char c = *iter;
            auto pr = char_map.insert({c,index});
            if(pr.second)
            {
                current_length+=1;
            }
            else{
                if(char_map[c]<start_index)
                {
                    char_map[c]=index; 
                    current_length+=1;
                }
                else
                {
                    start_index = char_map[c]+1;
                    char_map[c]=index;
                    current_length = index - start_index + 1;                    
                }
            }
            if(max_length<current_length)
            {
            max_length=current_length;
            }
            index++;
        }
        if(s.size()==1) max_length=1;
        return max_length;
    }
};
