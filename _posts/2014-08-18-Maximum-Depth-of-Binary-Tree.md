---
layout: post
title: Maximum Depth of Binary Tree
date: 2014-08-18 08:32:16
disqus: y
---

## 题意：
给一棵二叉树，求二叉树的最大深度

## 要求：
无

## 思路：
求二叉树的深度，用递归来做，注意判断root为空的条件

## 更新：
总结leetcode树的题目

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
    int maxDepth(TreeNode *root) {
        if(!root)
            return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
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
    def maxDepth(self, root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        
 {% endhighlight %}
