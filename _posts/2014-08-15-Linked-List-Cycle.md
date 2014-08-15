---
layout: post
title: Linked List Cycle
date: 2014-08-15 13:17:16
disqus: y
---

## 题意：
判断链表中有没有环

## 要求：
不使用额外空间

## 思路：
设置一个快指针和一个慢指针，快指针每次走两步，慢指针每次走一步，如果存在环，那么快指针一定可以追上慢指针

## 更新：
总结leetcode链表内容

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
    bool hasCycle(ListNode *head) {
        if(!head || !head->next)
        {
            return false;
        }
        ListNode *p=head;
        ListNode *q=head;
        while(p)
        {
            p=p->next;
            if(!q)
                return false;
            q=q->next;
            if(!q)
                return false;
            q=q->next;
            if(p==q)
                return true;
        }
        return false;
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
    # @return a boolean
    def hasCycle(self, head):
        if head==None:
            return False
        if head.next==None:
            return False
        if head.next.next==None:
            return False
        p=head
        q=head.next.next
        while p!=None and q!=None:
            if q.next==None:
                return False
            if q.next.next==None:
                return False
            if q.val==p.val:
                return True
            p=p.next
            q=q.next.next
        return False
        
 {% endhighlight %}
