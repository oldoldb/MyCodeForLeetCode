---
layout: post
title: Reorder List
date: 2014-08-14 13:32:16
disqus: y
---

## 题意：
将新区间插入到有序的区间中

## 要求：


## 思路：
http://blog.csdn.net/whuwangyi/article/details/14146461

1）把整个链表划分成2个等长的子链表，如果原链表长度为奇数，那么第一个子链表的长度多1。

2）翻转第二个子链表；

3）将两个子链表合并。

## 更新：
思路一致，自己重新做了一遍

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
    ListNode *reverseLinkedList(ListNode *head,ListNode *tail)
    {
        ListNode *phead=NULL;
        while(head!=tail)
        {
            ListNode *p=head->next;
            head->next=phead;
            phead=head;
            head=p;
        }
        return phead;
    }
    ListNode* findMiddle(ListNode *head)
    {
        if(!head || !head->next)
        {
            return NULL;
        }
        ListNode *p=head;
        ListNode *q=head;
        while(q)
        {
            p=p->next;
            if(!q)
                break;
            q=q->next;
            if(!q)
                break;
            q=q->next;
        }
        return p;
    }
    ListNode* merge(ListNode *head1,ListNode *head2)
    {
        ListNode *head=head1;
        ListNode *p=head;
        head1=head1->next;
        while(head2)
        {
            p->next=head2;
            p=head2;
            head2=head2->next;
            if(!head1)
                break;
            p->next=head1;
            p=head1;
            head1=head1->next;
        }
        p->next=NULL;
        return head;
    }
    void reorderList(ListNode *head)
    {
        if(!head || !head->next)
        {
            return;
        }
        ListNode *head2=findMiddle(head);
        head2=reverseLinkedList(head2,NULL);
        head=merge(head,head2);
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
    # @return nothing
    def reorderList(self, head):
        if head==None or head.next==None:
            return
        slow=head
        fast=head
        while fast.next!=None:
            fast=fast.next
            if fast.next!=None:
                fast=fast.next
            else:
                break
            slow=slow.next
        head1=head
        head2=slow.next
        slow.next=None
        cur=head2
        post=cur.next
        cur.next=None
        while post!=None:
            temp=post.next
            post.next=cur
            cur=post
            post=temp
        head2=cur
        p=head1
        q=head2
        while q!=None:
            temp1=p.next
            temp2=q.next
            p.next=q
            q.next=temp1
            p=temp1
            q=temp2
 {% endhighlight %}
