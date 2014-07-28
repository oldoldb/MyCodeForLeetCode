---
layout: post
title: Convert Sorted Array to Binary Search Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
将有序数组转换成平衡二叉树

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
    TreeNode *addNode(int l,int r,vector<int> &num,vector<bool> &visit)
    {
        int m=l+(r-l)/2;
        if(visit[m])
        {
            return NULL;
        }
        visit[m]=true;
        TreeNode *tempnode=new TreeNode(num[m]);
        tempnode->left=addNode(l,m,num,visit);
        tempnode->right=addNode(m,r,num,visit);
        return tempnode;
    }
    TreeNode *sortedArrayToBST(vector<int> &num) {
        if(num.size()==0)
        {
            return NULL;
        }
        int n=num.size();
        vector<bool>visit;
        visit.resize(n);
        TreeNode *root=new TreeNode(num[n/2]);
        visit[n/2]=true;
        root->left=addNode(0,n/2,num,visit);
        root->right=addNode(n/2,n,num,visit);
        return root;
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
