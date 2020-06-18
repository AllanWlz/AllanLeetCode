
// @Title: 两数相加 (Add Two Numbers)
// @Author: allan.wanglz@qq.com
// @Date: 2020-06-18 22:14:04
// @Runtime: 40 ms
// @Memory: 9.3 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
static int x = [](){ std::ios::sync_with_stdio(false); std::cin.tie(NULL); std::cout.tie(NULL); return NULL; }();
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *cl1=l1;
        ListNode *cl2=l2;
        ListNode *p = new ListNode((cl1->val+cl2->val)%10);
        ListNode *start = p;
        int jinwei=(cl1->val+cl2->val >= 10? 1:0);
        while(cl1->next!=NULL || cl2->next!= NULL)
        {
            if(cl1->next==NULL)
            {
                cl2 = cl2->next;
                int sum =  cl2->val + jinwei;
                ListNode *q =  new ListNode(sum%10);
                p->next = q;
                p = q;
                jinwei=(sum >= 10? 1:0);
                continue;
            }
            if(cl2->next==NULL)
            {
                cl1 = cl1->next;
                int sum =  cl1->val + jinwei;
                ListNode *q =  new ListNode(sum%10);
                p->next = q;
                p = q;
                jinwei=(sum >= 10? 1:0);
                continue;
            }
            cl1 = cl1->next;
            cl2 = cl2->next;
            int sum =  cl1->val + cl2->val + jinwei;
            ListNode *q =  new ListNode(sum%10);
            p->next = q;
            p = q;
            jinwei=(sum >= 10? 1:0);
        }
        if(jinwei != 0)
        {
             ListNode *q =  new ListNode(jinwei);
             p->next = q;
             p = q;            
        }
        return start;
    }
};
