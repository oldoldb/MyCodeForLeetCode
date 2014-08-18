---
layout: post
title: Binary Tree Maximum Path Sum
date: 2014-08-18 17:07:16
disqus: y
---

## 题意：
求树中任意两点路径的最大值

## 要求：


## 思路：
思路类似于求子数组的最大和，只不过这是在树上，对任意一个结点，分别递归求其左子树和右子树的最大值，根据正负判断是否要连接起来

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
    int ans=INT_MIN;
    int maxPath(TreeNode *root)
    {
        if(!root)
            return INT_MIN;
        int l=maxPath(root->left);
        int r=maxPath(root->right);
        int m=root->val;
        if(l>0)
            m+=l;
        if(r>0)
            m+=r;
        ans=max(ans,m);
        return max(max(l,r),0)+root->val;
    }
    int maxPathSum(TreeNode *root) {
        maxPath(root);
        return ans;
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
    # @return an integer
    def maxPathSum(self, root):
        if root==None:
            return 0
        self.ans=root.val
        self.dfs(root)
        return self.ans
    def dfs(self,root):
        if root==None:
            return -2147483648
        l=self.dfs(root.left)
        r=self.dfs(root.right)
        m=root.val
        if l>0:
            m+=l
        if r>0:
            m+=r
        self.ans=max(self.ans,m)
        return max(max(l,r),0)+root.val
 {% endhighlight %}
