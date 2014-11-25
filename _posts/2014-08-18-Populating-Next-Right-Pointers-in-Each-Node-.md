---
layout: post
title: Populating Next Right Pointers in Each Node 
date: 2014-08-18 18:33:16
disqus: y
---

## 题意：
构造next指针

## 要求：


## 思路：

##更新：
总结leetcode树的题目

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        TreeLinkNode *left=root;
        while(left)
        {
            TreeLinkNode *p=left;
            while(p)
            {
                if(p->left)
                    p->left->next=p->right;
                if(p->right)
                    p->right->next=p->next?p->next->left:NULL;
                p=p->next;
            }
            left=left->left;
        }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
‘’’
 Definition for a  binary tree node
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None
‘’’
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root==None:
            return 
        if root.left==None:
            return
        root.left.next=root.right
        if root.next==None:
            root.right.next=None
        else:
            root.right.next=root.next.left
        self.connect(root.left)
        self.connect(root.right)
 {% endhighlight %}
