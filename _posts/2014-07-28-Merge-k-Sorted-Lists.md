---
layout: post
title: Merge k Sorted Lists
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
合并K个有序链表

## 要求：


## 思路：
两种方法，一种是类似于合并排序，一种是维护一个堆
http://blog.csdn.net/linhuanmars/article/details/19899259

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class ListNodeCompare:public binary_function<ListNode*,ListNode*,bool>
{
public:
    bool operator()(ListNode* t1,ListNode *t2)const
    {
        if(!t1||!t2)
        {
            return !t2;
        }
        return t1->val>t2->val;
    }
};
class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if(lists.empty())
        {
            return NULL;
        }
        priority_queue<ListNode*,vector<ListNode*>,ListNodeCompare> pq;
        for(int i=0;i<lists.size();i++)
        {
            if(lists[i]!=NULL)
            {
                pq.push(lists[i]);
            }
        }
        ListNode phead(-1);
        ListNode *p=&phead;
        while(!pq.empty())
        {
            ListNode *q=pq.top();
            pq.pop();
            p->next=q;
            p=p->next;
            if(q->next)
            {
                pq.push(q->next);
            }
        }
        return phead.next;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if lists==None or len(lists)==0:
            return None
        return self.mergelist(lists,0,len(lists)-1)
    def mergelist(self,lists,l,r):
        if l<r:
            m = (l+r)/2
            return self.merge(self.mergelist(lists,l,m),self.mergelist(lists,m+1,r))
        return lists[l]
    def merge(self,l1,l2):
        dummy = ListNode(0)
        dummy.next=l1
        cur = dummy
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                l1=l1.next
            else:
                next=l2.next
                cur.next=l2
                l2.next=l1
                l2=next
            cur=cur.next
        if l2!=None:
            cur.next=l2
        return dummy.next
 {% endhighlight %}
