---
layout: post
title: Recover Binary Search Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
二叉搜索树中有两个结点的位置错了，将它转换为正确的二叉搜索树

## 要求：
空间复杂度O（1）

## 思路：
二叉搜索树用中序遍历可以得到有序排列，这样如果有结点的值小于前面结点的值，说明出现了错误，记录下来。

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
    TreeNode *pre;
    TreeNode *first;
    TreeNode *second;
    void inorder(TreeNode *root)
    {
        if(root==NULL)
        {
            return ;
        }
        inorder(root->left);
        if(pre!=NULL && pre->val>root->val)
        {
            if(first==NULL)
            {
                first = pre;
                second = root;
            }
            else
            {
                second = root;
            }
        }
        pre = root;
        inorder(root->right);
    }
    void recoverTree(TreeNode *root) {
        inorder(root);
        if(first!=NULL && second!=NULL)
        {
            swap(first->val,second->val);
        }
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
    # @return a tree node
    def recoverTree(self, root):
        self.pre = None
        self.first = None
        self.second = None
        self.inorder(root)
        if self.first!=None and self.second!=None:
            self.first.val, self.second.val = self.second.val, self.first.val
        return root
    def inorder(self,root):
        if root==None:
            return
        
        self.inorder(root.left)
        if self.pre!=None and self.pre.val>root.val:
            if self.first==None:
                self.first = self.pre
                self.second = root
            else:
                self.second = root
        self.pre = root
        self.inorder(root.right)
 {% endhighlight %}
