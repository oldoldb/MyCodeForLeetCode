---
layout: post
title: Unique Binary Search Trees II
date: 2014-08-18 11:06:16
disqus: y
---

## 题意：
求含n个节点的二叉树的所有形态

## 要求：


## 思路：
深搜，以每个节点为根，先搜左右子树的所有可能，然后再枚举这些可能的组合

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
    vector<TreeNode*> buildTree(int l, int r)
    {
        vector<TreeNode*>ans;
        if(l>r)
        {
            ans.push_back(NULL);
            return ans;
        }
        for(int i=l;i<=r;i++)
        {
            vector<TreeNode*>left=buildTree(l,i-1);
            vector<TreeNode*>right=buildTree(i+1,r);
            for(int j=0;j<left.size();j++)
            {
                for(int k=0;k<right.size();k++)
                {
                    TreeNode *root=new TreeNode(i+1);
                    root->left=left[j];
                    root->right=right[k];
                    ans.push_back(root);
                }
            }
        }
        return ans;
    }
    vector<TreeNode *> generateTrees(int n) {
        return buildTree(0,n-1);
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
    def buildTree(self,l,r):
        ans=[]
        if l>r:
            ans.append(None)
            return ans
        for i in range(l,r+1):
            left=self.buildTree(l,i-1)
            right=self.buildTree(i+1,r)
            for j in range(0,len(left)):
                for k in range(0,len(right)):
                    root=TreeNode(i+1)
                    ans.append(root)
                    root.left=left[j]
                    root.right=right[k]
        return ans
    # @return a list of tree node
    def generateTrees(self, n):
        return self.buildTree(0,n-1)
 {% endhighlight %}
