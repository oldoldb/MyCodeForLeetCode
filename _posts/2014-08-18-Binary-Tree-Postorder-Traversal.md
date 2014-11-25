---
layout: post
title: Binary Tree Postorder Traversal
date: 2014-08-18 10:34:16
disqus: y
---

## 题意：
树的后序遍历

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
    vector<int> postorderTraversal(TreeNode *root) {
        stack<TreeNode*>st;
        vector<int>ans;
        if(!root)
            return ans;
        st.push(root);
        TreeNode *prev=root;
        while(!st.empty())
        {
            TreeNode *cur=st.top();
            if(!cur->left&&!cur->right || cur->left==prev || cur->right==prev)
            {
                st.pop();
                ans.push_back(cur->val);
                prev=cur;
            }
            else
            {
                if(cur->right)
                    st.push(cur->right);
                if(cur->left)
                    st.push(cur->left);
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
    def postorderTraversal(self, root):
        ans=[]
        if root==None:
            return ans
        ans.extend(self.postorderTraversal(root.left))
        ans.extend(self.postorderTraversal(root.right))
        ans.append(root.val)
        return ans
 {% endhighlight %}
