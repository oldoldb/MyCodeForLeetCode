---
layout: post
title: Rotate List
date: 2014-08-15 21:36:06
disqus: y
---

## 题意：
右移链表

## 要求：


## 思路：
找到移动的位置改变头指针就好

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
    ListNode *rotateRight(ListNode *head, int k) {
        if(!head ||!head->next || !k)
            return head;
        ListNode *p=head;
        ListNode *q=head;
        int n=0;
        while(p)
        {
            n++;
            q=p;
            p=p->next;
        }
        p=head;
        k=k%n;
        k=n-k-1;
        while(k--)
            p=p->next;
        q->next=head;
        head=p->next;
        p->next=NULL;
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
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head==None or head.next==None or k==0:
            return head
        length=0
        p=head
        q=head
        while p!=None:
            length=length+1
            q=p
            p=p.next
        k = k % length
        p=head
        for i in range(length-k-1):
            p=p.next
        q.next=head
        head=p.next
        p.next=None
        return head
 {% endhighlight %}
