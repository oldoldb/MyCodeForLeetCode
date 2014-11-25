---
layout: post
title: Binary Tree Preorder Traversal
date: 2014-08-18 09:24:16
disqus: y
---

## 题意：
前序遍历

## 要求：
递归+非递归实现

## 思路：
只会递归实现，非递归后续来做
这里返回一个vector反而麻烦了许多

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
    vector<int> preorderTraversal(TreeNode *root) {
        stack<TreeNode*>st;
        vector<int>ans;
        while(!st.empty() || root)
        {
            if(root)
            {
                ans.push_back(root->val);
                if(root->right)
                    st.push(root->right);
                root=root->left;
            }
            else
            {
                root=st.top();
                st.pop();
            }
        }
        return ans;
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
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        ans=[]
        if root==None:
            return ans
        ans.append(root.val);
        ans.extend(self.preorderTraversal(root.left));
        ans.extend(self.preorderTraversal(root.right));
        return ans
 {% endhighlight %}
