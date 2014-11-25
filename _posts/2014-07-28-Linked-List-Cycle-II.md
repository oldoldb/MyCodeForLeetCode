---
layout: post
title: Linked List Cycle II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
找出链表中环的开始位置

## 要求：
不使用额外空间

## 思路：
证明看这里http://www.cnblogs.com/x1957/p/3406448.html

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
    ListNode *detectCycle(ListNode *head) {
        if(head==NULL)
        {
            return NULL;
        }
        if(head->next==NULL)
        {
            return NULL;
        }
        if(head->next->next==NULL)
        {
            return NULL;
        }
        ListNode *p=head;
        ListNode *q=head->next->next;
        while(p!=NULL&&q!=NULL)
        {
            if(p==q)
            {
                p=head;
                q=q->next->next;
                while(p!=q)
                {
                    p=p->next;
                    q=q->next;
                }
                return q;
            }
            if(q->next==NULL)
            {
                return NULL;
            }
            if(q->next->next==NULL)
            {
                return NULL;
            }
            p=p->next;
            q=q->next->next;
        }
        return NULL;
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
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head==None:
            return None
        if head.next==None:
            return None
        if head.next.next==None:
            return None
        p=head
        q=head.next.next
        while p!=None and q!=None:
            if q.next==None:
                return None
            if q.next.next==None:
                return None
            if q.val==p.val:
                p=head
                q=q.next.next
                while p!=q:
                    p=p.next
                    q=q.next
                return p
            p=p.next
            q=q.next.next
        return None
 {% endhighlight %}
