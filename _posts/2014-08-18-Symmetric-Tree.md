---
layout: post
title: Symmetric Tree
date: 2014-08-18 09:52:16
disqus: y
---

## 题意：
判断二叉树是否对称

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
    bool isSymmetric(TreeNode *root) {
        if(!root)
            return true;
        stack<TreeNode*>st1;
        stack<TreeNode*>st2;
        st1.push(root->left);
        st2.push(root->right);
        while(!st1.empty() && !st2.empty())
        {
            TreeNode *l=st1.top();
            st1.pop();
            TreeNode *r=st2.top();
            st2.pop();
            if(!l && !r)
                continue;
            else if(l && r)
            {
                if(l->val==r->val)
                {
                    st1.push(l->left);
                    st1.push(l->right);
                    st2.push(r->right);
                    st2.push(r->left);
                }
                else
                    return false;
            }
            else
                return false;
        }
        return true;
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
