---
layout: post
title: Reverse Nodes in k-Group
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
在单链表中，每K个一组，反转链表

## 要求：
只能使用连续空间

## 思路：
每K个调用一次反转链表子函数

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
    void reverse(ListNode **start,ListNode **end)
    {
        ListNode *p=*start;
        ListNode *prev=NULL;
        while(p!=*end)
        {
            ListNode *next=p->next;
            p->next=prev;
            prev=p;
            p=next;
        }
        p->next=prev;
    }
    ListNode *reverseKGroup(ListNode *head, int k) {
        if(head==NULL)
        {
            return NULL;
        }
        if(head->next==NULL)
        {
            return head;
        }
        if(k<=1)
        {
            return head;
        }
        ListNode *prev=NULL;
        ListNode *p=head;
        while(p!=NULL)
        {
            ListNode *q=p;
            for(int i=0;i<k-1;i++)
            {
                q=q->next;
                if(q==NULL)
                {
                    return head;
                }
            }
            ListNode *next=q->next;
            reverse(&p,&q);
            if(prev!=NULL)
            {
                prev->next=q;
            }
            else
            {
                head=q;
            }
            p->next=next;
            prev=p;
            p=next;
        }
        return head;
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
    def reverse(self,start,end):
        p=start
        prev=None
        while p!=end:
            next=p.next
            p.next=prev
            prev=p
            p=next
        p.next=prev
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head==None:
            return None
        if head.next==None:
            return head
        if k<=1:
            return head
        prev=None
        p=head
        while p!=None:
            q=p
            for i in range(k-1):
                q=q.next
                if q==None:
                    return head
            next=q.next
            self.reverse(p,q)
            if prev!=None:
                prev.next=q
            else:
                head=q
            p.next=next
            prev=p
            p=next
        return head
 {% endhighlight %}
