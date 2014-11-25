---
layout: post
title: Binary Tree Postorder Traversal
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
树的后序遍历

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
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int>ans;
        if(root==NULL)
        {
            return ans;
        }
        vector<int>temp=postorderTraversal(root->left);
        ans.insert(ans.end(),temp.begin(),temp.end());
        temp=postorderTraversal(root->right);
        ans.insert(ans.end(),temp.begin(),temp.end());
        ans.push_back(root->val);
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
