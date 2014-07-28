---
layout: post
title: Swap Nodes in Pairs
date: 2014-07-28 15:52:16
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
        if(head==NULL)
        {
            return NULL;
        }
        if(head->next==NULL)
        {
            return head;
        }
        ListNode *p=head;
        ListNode *q=head->next;
        p->next=q->next;
        q->next=p;
        head=q;
        ListNode *s=p;
        while(p!=NULL)
        {
            s=p;
            p=p->next;
            if(p==NULL)
            {
                break;
            }
            if(p->next==NULL)
            {
                s->next=p;
                break;
            }
            q=p->next;
            p->next=q->next;
            q->next=p;
            s->next=q;
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
