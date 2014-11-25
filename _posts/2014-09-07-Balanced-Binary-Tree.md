---
layout: post
title: Balanced Binary Tree
date: 2014-09-07 11:31:16
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
    bool isBalancedHelper(TreeNode *root, int &depth)
    {
        if(root==NULL)
        {
            depth=0;
            return true;
        }
        int left,right;
        if(isBalancedHelper(root->left, left) && isBalancedHelper(root->right, right))
        {
            int diff=abs(left-right);
            if(diff<=1)
            {
                depth=1+(left>right?left:right);
                return true;
            }
        }
        return false;
    }
    bool isBalanced(TreeNode *root) {
        int depth=0;
        return isBalancedHelper(root, depth);
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
