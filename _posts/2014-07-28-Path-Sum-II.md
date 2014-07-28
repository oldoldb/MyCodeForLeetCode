---
layout: post
title: Path Sum II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求二叉树中路径和为给定值的路径

## 要求：


## 思路：
深搜

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
    void dfs(TreeNode *root,int sum,int cnt,vector<int> &vec,vector<vector<int> > &ans)
    {

        if(sum==cnt&&root->left==NULL&&root->right==NULL)
        {
            ans.push_back(vec);
            return ;
        }
        if(root->left!=NULL)
        {
            vec.push_back(root->left->val);
            dfs(root->left,sum,cnt+root->left->val,vec,ans);
            vec.pop_back();
        }
        if(root->right!=NULL)
        {
            vec.push_back(root->right->val);
            dfs(root->right,sum,cnt+root->right->val,vec,ans);
            vec.pop_back();
        }
    }
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<vector<int> > ans;
        vector<int> vec;
        if(root==NULL)
        {
            return ans;
        }
        vec.push_back(root->val);
        dfs(root,sum,root->val,vec,ans);
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
    def dfs(self,root,sum,cnt,vec,ans):
        if sum==cnt and root.left==None and root.right==None:
            vec2=vec[:]
            ans.append(vec2)
            return
        if root.left!=None:
            vec.append(root.left.val)
            self.dfs(root.left,sum,cnt+root.left.val,vec,ans)
            vec.pop()
        if root.right!=None:
            vec.append(root.right.val)
            self.dfs(root.right,sum,cnt+root.right.val,vec,ans)
            vec.pop()
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        ans=[]
        vec=[]
        if root==None:
            return ans
        vec.append(root.val)
        self.dfs(root,sum,root.val,vec,ans)
        return ans
        
 {% endhighlight %}
