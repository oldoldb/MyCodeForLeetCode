---
layout: post
title: Construct Binary Tree from Preorder and Inorder Traversal
date: 2014-08-18 16:34:16
disqus: y
---

## 题意：
根据前序遍历和中序遍历构造树

## 要求：


## 思路：
前序遍历的第一个节点是根节点，在中序遍历中找该根节点的位置，则可以讲中序遍历结果分为左右子树，递归解决

## 更新：
总结leetcode树的代码

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
    TreeNode *buildTreeHelper(vector<int> &preorder,int l1,int r1,vector<int> &inorder,int l2,int r2)
    {
        if(l1>r1)
            return NULL;
        int val=preorder[l1];
        int index;
        for(int i=l2;i<=r2;i++)
        {
            if(inorder[i]==val)
            {
                index=i;
                break;
            }
        }
        TreeNode *root=new TreeNode(val);
        root->left=buildTreeHelper(preorder,l1+1,l1+1+index-l2-1,inorder,l2,index-1);
        root->right=buildTreeHelper(preorder,l1+1+index-l2,r1,inorder,index+1,r2);
        return root;
    }
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return buildTreeHelper(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
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
    def buildTreeRecursive(self,preorder,prel,prer,inorder,inl,inr):
        if prel>prer:
            return None
        val=preorder[prel]
        index=0
        for i in range(inl,inr+1):
            if inorder[i]==val:
                index=i
                break
        len=index-inl
        root=TreeNode(val)
        root.left=self.buildTreeRecursive(preorder,prel+1,prel+len,inorder,inl,index-1)
        root.right=self.buildTreeRecursive(preorder,prel+len+1,prer,inorder,index+1,inr)
        return root
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        return self.buildTreeRecursive(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
 {% endhighlight %}
