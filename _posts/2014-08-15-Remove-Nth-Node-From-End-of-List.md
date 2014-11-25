---
layout: post
title: Remove Nth Node From End of List
date: 2014-08-15 14:20:06
disqus: y
---

## 题意：
从链表中删除倒数第N个节点

## 要求：


## 思路：
快慢指针

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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        if(!head)
        {
            return head;
        }
        ListNode *p=head;
        ListNode *q=head;
        while(n--)
        {
            q=q->next;
        }
        if(!q)
            head=head->next;
        else
        {
            while(q->next)
            {
                p=p->next;
                q=q->next;
            }
            p->next=p->next->next;
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
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p=head
        q=head
        s=None
        for i in range(1,n):
            q=q.next
        while q.next!=None:
            s=p
            p=p.next
            q=q.next
        if s==None:
            head=p.next
        else:
            s.next=p.next
        return head


 {% endhighlight %}
