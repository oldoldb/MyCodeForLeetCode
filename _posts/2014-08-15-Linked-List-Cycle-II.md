---
layout: post
title: Linked List Cycle II
date: 2014-08-15 14:07:44
disqus: y
---

## 题意：
找出链表中环的开始位置

## 要求：
不使用额外空间

## 思路：
证明看这里http://www.cnblogs.com/x1957/p/3406448.html

## 更新
总结leetcode题目

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
        if(!head || !head->next)
            return NULL;
        ListNode *slow=head;
        ListNode *fast=head;
        while(slow)
        {
            slow=slow->next;
            if(!fast)
                return NULL;
            fast=fast->next;
            if(!fast)
                return NULL;
            fast=fast->next;
            if(slow==fast)
                break;
        }
        if(!slow)
            return NULL;
        while(head!=slow)
        {
            head=head->next;
            slow=slow->next;
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
