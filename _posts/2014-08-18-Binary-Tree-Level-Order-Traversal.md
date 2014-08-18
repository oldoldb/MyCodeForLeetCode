---
layout: post
title: Binary Tree Level Order Traversal
date: 2014-08-18 10:38:16
disqus: y
---

## 题意：
树的按层次遍历

## 要求：
返回每层的结果为一个集合

## 思路：
多设置一个集合来保存每层的值

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
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> >ans;
        if(!root)
            return ans;
        queue<vector<TreeNode*> >q;
        vector<TreeNode*>vec;
        vec.push_back(root);
        q.push(vec);
        while(!q.empty())
        {
            vec=q.front();
            q.pop();
            vector<TreeNode*>temp;
            vector<int>t;
            for(int i=0;i<vec.size();i++)
            {
                t.push_back(vec[i]->val);
                if(vec[i]->left)
                    temp.push_back(vec[i]->left);
                if(vec[i]->right)
                    temp.push_back(vec[i]->right);
            }
            if(!t.empty())
                ans.push_back(t);
            if(!temp.empty())
                q.push(temp);
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
    # @return a list of lists of integers
    def levelOrder(self, root):
        ans=[]
        q=[]
        if root==None:
            return ans
        vec=[]
        vec.append(root)
        q.append(vec)
        while len(q):
            vec=q.pop()
            temp=[]
            temp2=[]
            for i in range(len(vec)):
                temp.append(vec[i].val)
                if vec[i].left!=None:
                    temp2.append(vec[i].left)
                if vec[i].right!=None:
                    temp2.append(vec[i].right)
            if len(temp2):
                q.append(temp2)
            if len(temp):
                ans.append(temp)
        return ans
 {% endhighlight %}
