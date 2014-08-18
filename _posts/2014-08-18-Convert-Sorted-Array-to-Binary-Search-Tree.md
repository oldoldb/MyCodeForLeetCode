---
layout: post
title: Convert Sorted Array to Binary Search Tree
date: 2014-08-18 09:42:16
disqus: y
---

## 题意：
将有序数组转换成平衡二叉树

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
    TreeNode *sortedArrayToBSTHelper(vector<int> &num, int l, int r)
    {
        if(l>r)
            return NULL;
        int m=l+(r-l)/2;
        TreeNode *root=new TreeNode(num[m]);
        root->left=sortedArrayToBSTHelper(num,l,m-1);
        root->right=sortedArrayToBSTHelper(num,m+1,r);
        return root;
    }
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return sortedArrayToBSTHelper(num,0,num.size()-1);
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
    def addNode(self,l,r,num,visit):
        m=l+(r-l)/2
        if visit[m]:
            return None
        visit[m]=True
        tempnode=TreeNode(num[m])
        tempnode.left=self.addNode(l,m,num,visit)
        tempnode.right=self.addNode(m,r,num,visit)
        return tempnode
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        n=len(num)
        visit=[False for i in range(n)]
        root=TreeNode(num[n/2])
        visit[n/2]=True
        root.left=self.addNode(0,n/2,num,visit)
        root.right=self.addNode(n/2,n,num,visit)
        return root
 {% endhighlight %}
