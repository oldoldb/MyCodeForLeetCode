---
layout: post
title: Flatten Binary Tree to Linked List 
date: 2014-09-24 16:04:16
disqus: y
---

## 题意：
给一颗二叉树，flatten it

## 要求：


## 思路：
类似于前序遍历，递归

## 更新：
总结leetcode链表题目

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
    TreeNode *head=NULL;
    void flatten(TreeNode *root) {
        if(!root)
            return;
        if(head)
        {
            head->right=root;
            head->left=NULL;
        }
        TreeNode *temp=root->right;
        head=root;
        flatten(root->left);
        flatten(temp);
    }
};

// NonRecursive:
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
    TreeNode *head=NULL;
    void flatten(TreeNode *root) {
        while(root)
        {
        // Attatches the right sub-tree to the rightmost leaf of the left sub-tree:
            if(root->left)
            {
                TreeNode *rightMost = root->left;
                while(rightMost->right)
                    rightMost=rightMost->right;
                rightMost->right=root->right;
                // Makes the left sub-tree to the right sub-tree:
                root->right=root->left;
                root->left=NULL;
            }
            // Flatten the rest of the tree:
            root=root->right;
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
    # @return nothing, do it in place
    lastNode = None
    def flatten(self, root):
        if root==None:
            return
        if self.lastNode!=None:
            self.lastNode.left = None
            self.lastNode.right = root
        self.lastNode = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
 {% endhighlight %}
