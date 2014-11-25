---
layout: post
title: Remove Duplicates from Sorted List
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
从有序链表中删除重复节点

## 要求：


## 思路：
定义快慢两个指针，当快指针值不等于慢指针时，就将快指针接到慢指针后面，并让慢指针追上快指针

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
    ListNode *deleteDuplicates(ListNode *head) {
        if(head==NULL)
        {
            return NULL;
        }
        ListNode *p=head;
        ListNode *ans=p;
        if(head->next==NULL)
        {
            return head;
        }
        ListNode *q=p->next;
        while(p!=NULL)
        {
            if(q==NULL)
            {
                p->next=q;
                p=q;
                continue;
            }
            if(p->val!=q->val)
            {
                p->next=q;
                p=q;
            }
            q=q->next;
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
‘''
 Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
‘’’
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None:
            return None
        p=head
        if head.next==None:
            return head
        q=head.next
        ans=p
        while p!=None:
            if q==None:
                p.next=q
                p=q
                continue
            if p.val!=q.val:
                p.next=q
                p=q
            q=q.next
        return ans
 {% endhighlight %}
