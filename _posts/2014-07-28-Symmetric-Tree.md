---
layout: post
title: Symmetric Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
判断二叉树是否对称

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
    bool ok(TreeNode *l,TreeNode *r)
    {
        if(l==NULL&&r==NULL)
        {
            return true;
        }
        else if(l==NULL&&r!=NULL || l!=NULL&&r==NULL)
        {
            return false;
        }
        else
        {
            return ok(l->left,r->right)&&ok(l->right,r->left)&&l->val==r->val;
        }
    }
    bool isSymmetric(TreeNode *root) {
        if(root==NULL)
        {
            return true;
        }
        return ok(root->left,root->right);
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
    def ok(self,l,r):
        if l==None and r==None:
            return True
        elif l==None and r!=None or l!=None and r==None:
            return False
        else:
            return self.ok(l.left,r.right) and self.ok(l.right,r.left) and l.val==r.val
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        return self.ok(root.left,root.right)
 {% endhighlight %}
