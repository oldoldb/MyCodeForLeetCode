---
layout: post
title: Add Two Numbers
date: 2014-08-17 20:17:16
disqus: y
---

## 题意：
用链表模拟加法

## 要求：


## 思路：
注意细节，各种进位，各种为空


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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *head=NULL;
        ListNode *p=NULL;
        int flag=0;
        while(l1||l2)
        {
            int val1=0;
            int val2=0;
            if(l1)
            {
                val1=l1->val;
                l1=l1->next;
            }
            if(l2)
            {
                val2=l2->val;
                l2=l2->next;
            }
            int val=val1+val2+flag;
            if(val>9)
            {
                val=val-10;
                flag=1;
            }
            else
                flag=0;
            ListNode *t=new ListNode(val);
            if(!p)
                head=t;
            else
                p->next=t;
            p=t;
        }
        if(flag)
            p->next=new ListNode(flag);
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
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        p = head
        flag = 0
        while l1!=None or l2!=None:
            val1 = l1.val if l1!=None else 0
            val2 = l2.val if l2!=None else 0
            val = val1 + val2 + flag
            p.val = val % 10
            flag = 1 if val>9 else 0
            if l1!=None:
                l1 = l1.next if l1.next!=None else None
            if l2!=None:
                l2 = l2.next if l2.next!=None else None
            if l1!=None or l2!=None or flag==1:
                p.next = ListNode(flag)
                p = p.next
        return head
 {% endhighlight %}
