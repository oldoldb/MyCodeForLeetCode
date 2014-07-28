---
layout: post
title: Copy List with Random Pointer
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
链表中每个结点有一个随机指针指向某个结点，复制这个链表

## 要求：


## 思路：
http://www.w3c.com.cn/copy-list-with-random-pointer-leetcode

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
        if(head==NULL)
        {
            return head;
        }
        RandomListNode *node = head;
        while(node!=NULL)
        {
            RandomListNode *newNode = (struct RandomListNode*)malloc(sizeof(struct RandomListNode));
            newNode = new RandomListNode(node->label);
            newNode->next = node->next;
            node->next = newNode;
            node = newNode->next;
        }
        node = head;
        while(node!=NULL)
        {
            if(node->random!=NULL)
            {
                node->next->random = node->random->next;
            }
            node = node->next->next;
        }
        RandomListNode *newHead = head->next;
        node = head;
        while(node!=NULL)
        {
            RandomListNode *newNode = (struct RandomListNode*)malloc(sizeof(struct RandomListNode));
            newNode = node->next;
            node->next = newNode->next;
            if(newNode->next!=NULL)
            {
                newNode->next = newNode->next->next;
            }
            node = node->next;
        }
        return newHead;
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
