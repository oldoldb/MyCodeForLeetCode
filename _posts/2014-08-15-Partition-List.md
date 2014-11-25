---
layout: post
title: Partition List 
date: 2014-08-15 15:57:16
disqus: y
---

## 题意：
划分单链表，使小于Target的结点在左，大于等于Target的结点在右

## 要求：


## 思路：
模拟,用两个链表分别记录<x的节点和>=x的节点

## 更新：
总结leetcode链表题目

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
        if(!head)
            return head;
        ListNode *l1,*l2;
        ListNode *head1=NULL,*head2=NULL;
        ListNode *p=head;
        while(p)
        {
            if(p->val<x)
            {
                if(!head1)
                    head1=p;
                else
                    l1->next=p;
                l1=p;
            }
            else
            {
                if(!head2)
                    head2=p;
                else
                    l2->next=p;
                l2=p;
            }
            p=p->next;
        }
        if(!head1)
            return head2;
        l1->next=head2;
        if(head2)
            l2->next=NULL;
        return head1;
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
