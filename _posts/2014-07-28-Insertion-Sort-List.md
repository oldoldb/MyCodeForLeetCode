---
layout: post
title: Insertion Sort List
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
用单链表模拟插入排序

## 要求：


## 思路：
为方便表示可以预设一个超级节点指向head

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
        if(head==NULL)
        {
            return NULL;
        }
        if(head->next==NULL)
        {
            return head;
        }
        ListNode *prev=head;
        ListNode *cur=head->next;
        ListNode *pprev=new ListNode(0);
        pprev->next=head;
        while(cur!=NULL)
        {
            if(cur->val>=prev->val)
            {
                prev=cur;
                cur=cur->next;
            }
            else
            {
                ListNode *s=pprev;
                ListNode *p=s->next;
                while(p->val<cur->val)
                {
                    s=p;
                    p=p->next;
                }
                prev->next=cur->next;
                cur->next=p;
                s->next=cur;
                cur=prev->next;
            }
        }
        return pprev->next;
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
