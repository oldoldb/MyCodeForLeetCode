---
layout: post
title: Reverse Linked List II 
date: 2014-08-14 08:55:12
disqus: y
---

## 题意：
反转链表中的指定范围

## 要求：


## 思路：

## 更新:

昨晚把反转链表彻底搞明白了，今天用自己的思路来过一遍链表的题目

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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        if(!head || !head->next || m==n)
        {
            return head;
        }
        ListNode *p=head;
        ListNode *prev=NULL;
        ListNode *pm;
        ListNode *pn;
        int cnt=0;
        while(p)
        {
            cnt++;
            if(cnt==m)
            {
                prev=s;
                pm=p;
            }
            if(cnt==n)
            {
                pn=p->next;
            }
            s=p;
            p=p->next;
        }
        ListNode *phead=pm;
        p=phead->next;
        ListNode *q=p->next;
        while(p!=pn)
        {
            p->next=phead;
            phead=p;
            p=q;
            if(q)
                q=q->next;
        }
        if(prev)
            prev->next=phead;
        else
            head=phead;
        pm->next=pn;
        return head;
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
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head==None:
            return None
        p=head
        q=None
        for i in range(1,m):
            q=p
            p=p.next
        now=p
        prev=p
        p=p.next
        for i in range(m,n):
            next=p.next
            p.next=prev
            prev=p
            p=next
        now.next=p
        if q:
            q.next=prev
        else:
            head=prev
        return head
 {% endhighlight %}
