
// @Title: 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:15:42
// @Runtime: 24 ms
// @Memory: 8.5 MB



class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> short_arr;
        vector<int> long_arr;
        if(nums1.size()<nums2.size())
        {
            short_arr = nums1;
            long_arr = nums2;
        }
        else
        {
            short_arr = nums2;
            long_arr = nums1;
        }
        int short_lo = 0;
        int long_lo = 0;
        int short_hi = short_arr.size();
        int long_hi = long_arr.size();
        double middle;
        
        while(short_hi - short_lo > 2)
        {
            int short_mi = (short_hi + short_lo) / 2;
            int long_mi = (long_hi + long_lo) / 2;
            if(short_arr[short_mi]>=long_arr[long_mi])
            {
                int step = min(short_hi-short_mi-1, long_mi - long_lo);
                long_lo = long_lo + step;
                short_hi = short_hi - step;
            }
            if(short_arr[short_mi]<long_arr[long_mi])
            {
                int step = 1;
                if((short_hi - short_lo) % 2 == 0)
                {
                   step = min(short_mi-short_lo-1, long_hi - long_mi - 1);                     
                }
                else
                {
                   step = min(short_mi-short_lo, long_hi - long_mi - 1);
                }
                long_hi = long_hi - step;
                short_lo = short_lo + step;
            }
        }
        
        int long_mi = (long_hi + long_lo) / 2;
        
        if(long_hi - long_lo < 5)
        {
            middle = find_median(short_arr, short_lo, short_hi, long_arr, long_lo, long_hi);
            return middle;
        }
        else{
            if((long_hi - long_lo) % 2 == 0)
            {
                middle = find_median(short_arr, short_lo, short_hi, long_arr, long_mi-2, long_mi+2);
                return middle;
            }
            else
            {
                middle = find_median(short_arr, short_lo, short_hi, long_arr, long_mi-1, long_mi+2);
                return middle;                
            }
        }
        
    }
    
    double find_median(vector<int> v1, int v1_lo, int v1_hi, vector<int> v2, int v2_lo, int v2_hi)
    {
        vector<int> p = vector<int>();
        p.insert(p.end(), v1.begin() + v1_lo, v1.begin() + v1_hi);
        p.insert(p.end(), v2.begin() + v2_lo, v2.begin() + v2_hi);
        sort(p.begin(), p.end());
        int p_mi = p.size() / 2;
        if(p.size() % 2 == 0)
        {
            return (p[p_mi] + p[p_mi-1])/2.0;
        }
        else
        {
            return p[p_mi] * 1.0;
        }
    }
};
