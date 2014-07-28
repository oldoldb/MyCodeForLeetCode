---
layout: post
title: Populating Next Right Pointers in Each Node 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
构造next指针

## 要求：


## 思路：


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
       if(root==NULL)
       {
           return ;
       }
       if(root->left==NULL)
       {
           return ;
       }
       root->left->next=root->right;
       root->right->next=root->next==NULL?NULL:root->next->left;
       connect(root->left);
       connect(root->right);
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
