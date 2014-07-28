---
layout: post
title: Reorder List
date: 2014-07-28 15:52:16
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
    void reorderList(ListNode *head) {
        if(head==NULL || head->next==NULL)
        {
            return;
        }
        ListNode *slow=head;
        ListNode *fast=head;
        while(fast->next!=NULL)
        {
            fast=fast->next;
            if(fast->next!=NULL)
            {
                fast=fast->next;
            }
            else
            {
                break;
            }
            slow=slow->next;
        }
        ListNode *head1=head;
        ListNode *head2=slow->next;
        slow->next=NULL;
        ListNode *cur=head2;
        ListNode *post=cur->next;
        cur->next=NULL;
        while(post!=NULL)
        {
            ListNode *temp=post->next;
            post->next=cur;
            cur=post;
            post=temp;
        }
        head2=cur;
        ListNode *p=head1;
        ListNode *q=head2;
        while(q!=NULL)
        {
            ListNode *temp1=p->next;
            ListNode *temp2=q->next;
            p->next=q;
            q->next=temp1;
            p=temp1;
            q=temp2;
        }
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
