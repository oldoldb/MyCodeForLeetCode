---
layout: post
title: Balanced Binary Tree
date: 2014-08-18 09:3:16
disqus: y
---

## 题意：
判断二叉树是否位高度平衡的，高度平衡定义为任一节点的 两棵子树的高度差不超过1

## 要求：


## 思路：
递归

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
    int maxDepth(TreeNode *root)
    {
        if(!root)
            return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
    bool isBalanced(TreeNode *root) {
        if(!root)
            return true;
        return abs(maxDepth(root->left)-maxDepth(root->right))<=1 && isBalanced(root->left) && isBalanced(root->right);
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
‘''
class Solution:
    def getDepth(self,root):
        if root==None:
            return 0
        return max(self.getDepth(root.left),self.getDepth(root.right))+1
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root==None:
            return True
        l=self.getDepth(root.left)
        r=self.getDepth(root.right)
        return abs(l-r)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
 {% endhighlight %}
