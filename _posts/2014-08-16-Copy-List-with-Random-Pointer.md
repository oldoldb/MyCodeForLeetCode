---
layout: post
title: Copy List with Random Pointer
date: 2014-08-16 10:08:12
disqus: y
---

## 题意：
链表中每个结点有一个随机指针指向某个结点，复制这个链表

## 要求：


## 思路：
http://www.w3c.com.cn/copy-list-with-random-pointer-leetcode

## 更新：
总结leetcode链表题目

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(!head)
            return head;
        RandomListNode *p=head;
        while(p)
        {
            RandomListNode *q=p->next;
            p->next=new RandomListNode(p->label);
            p->next->next=q;
            p=q;
        }
        p=head;
        while(p)
        {
            p->next->random=p->random==NULL?NULL:p->random->next;
            p=p->next->next;
        }
        p=head;
        RandomListNode *r=head->next;
        RandomListNode *q=r;
        while(true)
        {
            p->next=q->next;
            p=p->next;
            if(!p)
                break;
            q->next=p->next;
            q=q->next;
        }
        return r;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return head
        node = head
        while node != None:
            newNode = RandomListNode(node.label)
            newNode.next = node.next
            node.next = newNode
            node = newNode.next
        node = head
        while node != None:
            if node.random != None:
                node.next.random = node.random.next
            node = node.next.next
        newHead = head.next
        node = head
        while node != None:
            newNode = node.next
            node.next = newNode.next
            if newNode.next != None:
                newNode.next = newNode.next.next
            node = node.next
        return newHead
 {% endhighlight %}
