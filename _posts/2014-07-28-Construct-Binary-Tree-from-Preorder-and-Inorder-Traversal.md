---
layout: post
title: Construct Binary Tree from Preorder and Inorder Traversal
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
根据前序遍历和中序遍历构造树

## 要求：


## 思路：
前序遍历的第一个节点是根节点，在中序遍历中找该根节点的位置，则可以讲中序遍历结果分为左右子树，递归解决

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
    TreeNode *buildTree(vector<int> &preorder,int prel,int prer,vector<int> &inorder,int inl,int inr)
    {
        if(prel>prer)
        {
            return NULL;
        }
        int val=preorder[prel];
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
        root->left=buildTree(preorder,prel+1,prel+len,inorder,inl,index-1);
        root->right=buildTree(preorder,prel+len+1,prer,inorder,index+1,inr);
        return root;
    }
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        if(preorder.size()==0)
        {
            return NULL;
        }
        return buildTree(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
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
