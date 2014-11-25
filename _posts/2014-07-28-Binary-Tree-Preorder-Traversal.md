---
layout: post
title: Binary Tree Preorder Traversal
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
前序遍历

## 要求：
递归+非递归实现

## 思路：
只会递归实现，非递归后续来做
这里返回一个vector反而麻烦了许多

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
        vector<int>vec,vec1,vec2;
        if(root==NULL)
        {
            return vec;
        }
        
        vec.push_back(root->val);
        vec1=preorderTraversal(root->left);
        vec2=preorderTraversal(root->right);
        vec.insert(vec.end(),vec1.begin(),vec1.end());
        vec.insert(vec.end(),vec2.begin(),vec2.end());
        vec1.clear();
        vec2.clear();
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
