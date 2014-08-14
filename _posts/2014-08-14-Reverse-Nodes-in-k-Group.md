---
layout: post
title: Reverse Nodes in k-Group
date: 2014-08-14 12:3:08
disqus: y
---

## 题意：
在单链表中，每K个一组，反转链表

## 要求：
只能使用连续空间

## 思路：
每K个调用一次反转链表子函数

## 更新：
真正弄明白了链表逆置

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
    ListNode *reverseLinkedList(ListNode *head,ListNode *tail)
    {
        ListNode *phead=NULL;
        while(head!=tail)
        {
            ListNode *p=head->next;
            head->next=phead;
            phead=head;
            head=p;
        }
        return phead;
    }
    ListNode *reverseKGroup(ListNode *head, int k)
    {
        if(!head || !head->next || k==1)
        {
            return head;
        }
        int cnt=0;
        ListNode *s=head;
        ListNode *prev=NULL;
        while(s)
        {
            s=s->next;
            cnt++;
            if(cnt==k)
            {
                ListNode *pm=prev==NULL?head:prev->next;
                ListNode *pn=s;
                ListNode *phead=reverseLinkedList(pm,pn);
                if(prev==NULL)
                    head=phead;
                else
                {
                    prev->next=phead;
                }
                pm->next=pn;
                prev=pm;
                cnt=0;
            }
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
