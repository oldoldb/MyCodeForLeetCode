---
layout: post
title: Remove Duplicates from Sorted List II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
删除单链表中重复出现过的节点

## 要求：


## 思路：
设置三个指针,s,p,q分别指向上一个节点，当前节点，下一个节点，不断更新，如果p和q所指的节点的值相同，那么让q指向后面第一个不同的点，然后直接删掉中间部分
为了处理1->1这种情况，设置一个超级节点指向head

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
    ListNode *deleteDuplicates(ListNode *head) {
        if(head==NULL)
        {
            return NULL;
        }
        if(head->next==NULL)
        {
            return head;
        }
        ListNode *pprev=new ListNode(-1);
        ListNode *s=pprev;
        ListNode *p=head;
        ListNode *q=head->next;
        pprev->next=head;
        while(q!=NULL)
        {
            if(p->val!=q->val)
            {
                s=p;
                p=q;
                q=q->next;
            }
            else
            {
                while(q!=NULL&&q->val==p->val)
                {
                    q=q->next;
                }
                if(q==NULL)
                {
                    s->next=NULL;
                }
                else
                {
                    p=q;
                    q=q->next;
                    s->next=p;
                }
            }
        }
        return pprev->next;
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
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None:
            return None
        if head.next==None:
            return head
        pprev=ListNode(-1)
        s=pprev
        p=head
        q=head.next
        pprev.next=head
        while q!=None:
            if p.val!=q.val:
                s=p
                p=q
                q=q.next
            else:
                while q!=None and q.val==p.val:
                    q=q.next
                if q==None:
                    s.next=None
                else:
                    p=q
                    q=q.next
                    s.next=p
        return pprev.next
 {% endhighlight %}
