---
layout: post
title: Add Two Numbers
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
用链表模拟加法

## 要求：


## 思路：
注意细节，各种进位，各种为空

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
        ListNode *head = new ListNode(0);
        ListNode *p = head;
        int flag=0;
        while(l1!=NULL || l2!=NULL)
        {
            int val1 = l1==NULL?0:l1->val;
            int val2 = l2==NULL?0:l2->val;
            int val = val1 + val2 + flag;
            p->val = val%10;
            flag = val>9?1:0;
            if(l1)
            {
                l1 = l1->next?l1->next:NULL;
            }
            if(l2)
            {
                l2 = l2->next?l2->next:NULL;
            }
            if(l1 || l2 || flag)
            {
                p->next = new ListNode(flag);
                p = p->next;
            }
        }
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
