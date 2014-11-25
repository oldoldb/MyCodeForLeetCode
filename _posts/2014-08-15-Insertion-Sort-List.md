---
layout: post
title: Insertion Sort List
date: 2014-08-15 21:14:16
disqus: y
---

## 题意：
用单链表模拟插入排序

## 要求：


## 思路：
为方便表示可以预设一个超级节点指向head

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
    ListNode *insertionSortList(ListNode *head) {
        if(!head || !head->next)
            return head;
        ListNode *qhead=head;
        ListNode *q=head;
        ListNode *p=head->next;
        while(p)
        {
            bool flag=false;
            ListNode *s=qhead;
            ListNode *prev=NULL;
            while(s!=p)
            {
                if(s->val<=p->val)
                {
                    prev=s;
                    s=s->next;
                }
                else
                {
                    flag=true;
                    ListNode *t=p->next;
                    q->next=t;
                    if(s==qhead)
                    {
                        p->next=qhead;
                        qhead=p;
                    }
                    else
                    {
                        prev->next=p;
                        p->next=s;
                    }
                    p=t;
                    break;
                }
            }
            if(!flag)
            {
                q->next=p;
                q=p;
                p=p->next;
                q->next=p;
            }
        }
        return qhead;
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
    # @return a ListNode
    def insertionSortList(self, head):
        if head==None:
            return None
        if head.next==None:
            return head
        prev=head
        cur=head.next
        pprev=ListNode(-1)
        pprev.next=head
        while cur!=None:
            if cur.val>=prev.val:
                prev=cur
                cur=cur.next
            else:
                s=pprev
                p=s.next
                while p.val<cur.val:
                    s=p
                    p=p.next
                prev.next=cur.next
                cur.next=p
                s.next=cur
                cur=prev.next
        return pprev.next
 {% endhighlight %}
