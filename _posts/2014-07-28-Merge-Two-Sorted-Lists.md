---
layout: post
title: Merge Two Sorted Lists
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
合并有序链表

## 要求：


## 思路：


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
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *ans;
        if(l1==NULL&&l2==NULL)
        {
            return NULL;
        }
        else if(l1==NULL)
        {
            return l2;
        }
        else if(l2==NULL)
        {
            return l1;
        }
        else if(l1->val<l2->val)
        {
            ans=l1;
            l1=l1->next;
        }
        else
        {
            ans=l2;
            l2=l2->next;
        }
        ListNode *p=ans;
        while(l1!=NULL&&l2!=NULL)
        {
            if(l1->val<l2->val)
            {
                p->next=l1;
                p=p->next;
                l1=l1->next;
            }
            else
            {
                p->next=l2;
                p=p->next;
                l2=l2->next;
            }
        }
        
        if(l1!=NULL)
        {
            p->next=l1;
        }
        else
        {
            p->next=l2;
        }
        
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
‘’’
 Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
‘’’
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        ans=l1
        if l1==None and l2==None:
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1
        elif l1.val<l2.val:
            ans=l1
            l1=l1.next
        else:
            ans=l2
            l2=l2.next
        p=ans
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                p.next=l1
                p=p.next
                l1=l1.next
            else:
                p.next=l2
                p=p.next
                l2=l2.next
        if l1!=None:
            p.next=l1
        else:
            p.next=l2
        return ans
            
 {% endhighlight %}
