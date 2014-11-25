---
layout: post
title: Construct Binary Tree from Inorder and Postorder Traversal
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
根据中序遍历和后序遍历构造树

## 要求：


## 思路：
后序遍历的最后一个节点是根节点，到中序遍历中找到根节点，则划分为左右子树，递归操作

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
    TreeNode *buildTree(vector<int> &inorder,int inl,int inr,vector<int> &postorder,int postl,int postr)
    {
        if(inl>inr)
        {
            return NULL;
        }
        int val=postorder[postr];
        int index;
        for(int i=inl;i<=inr;i++)
        {
            if(inorder[i]==val)
            {
                index=i;
                break;
            }
        }
        int len=index-inl;
        TreeNode *root=new TreeNode(val);
        root->left=buildTree(inorder,inl,index-1,postorder,postl,postl+len-1);
        root->right=buildTree(inorder,index+1,inr,postorder,postl+len,postr-1);
        return root;
    }
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        if(inorder.size()==0)
        {
            return NULL;
        }
        return buildTree(inorder,0,inorder.size()-1,postorder,0,postorder.size()-1);
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
    def buildTreeRecursive(self,inorder,inl,inr,postorder,postl,postr):
        if inl>inr:
            return None
        val=postorder[postr]
        index=0
        for i in range(inl,inr+1):
            if inorder[i]==val:
                index=i
                break
        len=index-inl
        root=TreeNode(val)
        root.left=self.buildTreeRecursive(inorder,inl,index-1,postorder,postl,postl+len-1)
        root.right=self.buildTreeRecursive(inorder,index+1,inr,postorder,postl+len,postr-1)
        return root
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder)==0:
            return None
        return self.buildTreeRecursive(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)
 {% endhighlight %}
