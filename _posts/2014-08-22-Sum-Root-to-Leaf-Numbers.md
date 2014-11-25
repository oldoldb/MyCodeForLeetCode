---
layout: post
title: Sum Root to Leaf Numbers
date: 2014-08-22 08:22:16
disqus: y
---

## 题意：
求树中从根节点到叶节点所组成所有数字的和

## 要求：
无

## 思路：
深搜

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
    int sumNumbers(TreeNode *root) {
        int ans=0;
        if(!root)
            return ans;
        queue<TreeNode*> qTree;
        queue<int> qNum;
        qTree.push(root);
        qNum.push(root->val);
        while(!qTree.empty())
        {
            TreeNode *s=qTree.front();
            qTree.pop();
            int cur=qNum.front();
            qNum.pop();
            if(!s->left && !s->right)
                ans+=cur;
            if(s->right)
            {
                qTree.push(s->right);
                qNum.push(cur*10+s->right->val);
            }
            if(s->left)
            {
                qTree.push(s->left);
                qNum.push(cur*10+s->left->val);
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
    def dfs(self,root,sum,ans):
        if root.left==None and root.right==None:
            sum=sum*10+root.val
            ans[0]+=sum
            return 
        sum=sum*10+root.val
        if root.left!=None:
            self.dfs(root.left,sum,ans)
        if root.right!=None:
            self.dfs(root.right,sum,ans)
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root==None:
            return 0
        ans=[0]
        self.dfs(root,0,ans)
        return ans[0]
 {% endhighlight %}
