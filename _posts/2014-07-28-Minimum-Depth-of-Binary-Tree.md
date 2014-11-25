---
layout: post
title: Minimum Depth of Binary Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求二叉树的最小深度

## 要求：
无

## 思路：
递归

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode *root) {
        if(root==NULL)
        {
            return 0;
        }
        if(root->left==NULL&&root->right==NULL)
        {
            return 1;
        }
        else if(root->left==NULL&&root->right!=NULL)
        {
            return minDepth(root->right)+1;
        }
        else if(root->left!=NULL&&root->right==NULL)
        {
            return minDepth(root->left)+1;
        }
        else
        {
            return min(minDepth(root->left),minDepth(root->right))+1;
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
‘’’
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        elif root.left==None and root.right!=None:
            return self.minDepth(root.right)+1
        elif root.left!=None and root.right==None:
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
 {% endhighlight %}
