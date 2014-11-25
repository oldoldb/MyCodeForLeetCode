---
layout: post
title: Validate Binary Search Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
判断一棵树是不是二叉搜索树

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
    bool ok(TreeNode *root, int left, int right)
    {
        if(root==NULL)
        {
            return true;
        }
        return left<root->val && right>root->val && ok(root->left,left,root->val) && ok(root->right, root->val,right);
    }
    bool isValidBST(TreeNode *root) {
        return ok(root, INT_MIN, INT_MAX);
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.ok(root, -2147483648, 2147483647)
    def ok(self,root,left,right):
        if root==None:
            return True
        return root.val > left and root.val < right and self.ok(root.left,left, root.val) and self.ok(root.right,root.val,right)
 {% endhighlight %}
