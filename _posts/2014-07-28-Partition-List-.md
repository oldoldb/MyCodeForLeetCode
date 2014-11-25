---
layout: post
title: Partition List 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
划分单链表，使小于Target的结点在左，大于等于Target的结点在右

## 要求：


## 思路：
模拟,用两个链表分别记录<x的节点和>=x的节点

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
    ListNode *partition(ListNode *head, int x) {
        if(head==NULL)
        {
            return NULL;
        }
        ListNode *l=new ListNode(0);
        ListNode *r=new ListNode(0);
        ListNode *p=l;
        ListNode *q=r;
        while(head!=NULL)
        {
            if(head->val<x)
            {
                p->next=head;
                p=p->next;
                head=head->next;
                p->next=NULL;
            }
            else
            {
                q->next=head;
                q=q->next;
                head=head->next;
                q->next=NULL;
            }
        }
        p->next=r->next;
        return l->next;
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
‘’'
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head==None:
            return None
        p=l=ListNode(0)
        q=r=ListNode(0)
        prev=None
        cur=head
        while cur!=None:
            prev=cur
            cur=cur.next
            if prev.val<x:
                p.next=prev
                p=prev
                p.next=None
            else:
                q.next=prev
                q=prev
                q.next=None
        p.next=r.next
        return l.next
 {% endhighlight %}
