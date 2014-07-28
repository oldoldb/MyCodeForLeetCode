---
layout: post
title: Reverse Linked List II 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
反转链表中的指定范围

## 要求：


## 思路：
同3Sum Closest，只不过要加一个判重

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
        if(head==NULL)
        {
            return NULL;
        }
        ListNode *p=head;
        ListNode *q=NULL;
        for(int i=1;i<m;i++)
        {
            q=p;
            p=p->next;
        }
        ListNode *now=p;//记录反转后的末位置
        ListNode *prev=p;
        p=p->next;
        for(int i=m;i<n;i++)//将该段链表逆置
        {
            ListNode *next=p->next;
            p->next=prev;
            prev=p;
            p=next;
        }
        now->next=p;//尾
        if(q)//头
        {
            q->next=prev;
        }
        else
        {
            head=prev;
        }
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
