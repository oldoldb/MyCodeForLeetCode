---
layout: post
title: Swap Nodes in Pairs
date: 2014-08-17 19:53:36
disqus: y
---

## 题意：
交换链表中每两个邻接节点

## 要求：
不能只交换值，需要真正交换节点
只能使用连续存储空间

## 思路：
对于1->2->3->4的情况
假设现在要交换3和4
那么让s指向2,p指向3,q指向4
那么
p->next=q->next
q->next=p
s->next=q
即可
注意头两个节点的特殊情况

## 更新
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
    ListNode *swapPairs(ListNode *head) {
        if(!head || !head->next)
            return head;
        ListNode *s=head;
        ListNode *p=head;
        ListNode *prev=NULL;
        ListNode *phead=NULL;
        while(p)
        {
            if(!p->next)
                return phead;
            else
            {
                s=p;
                p=p->next;
                ListNode *t=p->next;
                if(prev)
                    prev->next=p;
                p->next=s;
                s->next=t;
                if(!phead) 
                    phead=p;
                prev=s;
                p=t;
            }
        }
        return phead;
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
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head==None:
            return None
        if head.next==None:
            return head
        p=head
        q=head.next
        p.next=q.next
        q.next=p
        head=q
        while p!=None:
            s=p
            p=p.next
            if p==None:
                break
            q=p.next
            if q==None:
                s.next=p
                break
            p.next=q.next
            q.next=p
            s.next=q
        return head
 {% endhighlight %}
