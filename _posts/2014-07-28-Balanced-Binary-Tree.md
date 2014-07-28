---
layout: post
title: Balanced Binary Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
判断二叉树是否位高度平衡的，高度平衡定义为任一节点的 两棵子树的高度差不超过1

## 要求：


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
    int getDepth(TreeNode *root)
    {
        if(root==NULL)
        {
            return 0;
        }
        int ldepth=getDepth(root->left);
        int rdepth=getDepth(root->right);
        return max(ldepth,rdepth)+1;
    }
    bool isBalanced(TreeNode *root) {
        if(root==NULL)
        {
            return true;
        }
        int ldepth=getDepth(root->left);
        int rdepth=getDepth(root->right);
        return isBalanced(root->left)&&isBalanced(root->right)&&abs(ldepth-rdepth)<=1;
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
