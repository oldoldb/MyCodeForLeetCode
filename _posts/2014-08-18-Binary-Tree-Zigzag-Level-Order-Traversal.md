---
layout: post
title: Binary Tree Zigzag Level Order Traversal
date: 2014-08-18 11:17:16
disqus: y
---

## 题意：
按Zigzag次序按层次遍历树

## 要求：


## 思路：
同普通的按层次遍历树，加一个是否reverse标记就好

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
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        vector<vector<int> >ans;
        if(!root)
            return ans;
        queue<vector<TreeNode*> >q;
        vector<TreeNode*>vec;
        vec.push_back(root);
        q.push(vec);
        bool flag=false;
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
            {
                if(flag)
                    reverse(t.begin(),t.end());
                flag=!flag;
                ans.push_back(t);
            }
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
    def zigzagLevelOrder(self, root):
        ans=[]
        if root==None:
            return ans 
        q=[]
        s=[]
        
        
        s.append(root)
        q.append(s)
        flag=True
        while len(q):
            s=q.pop()
            temp=[]
            temp2=[]
            for i in range(len(s)):
                temp.append(s[i].val)
                if s[i].left!=None:
                    temp2.append(s[i].left)
                if s[i].right!=None:
                    temp2.append(s[i].right)
            if len(temp):
                if flag:
                    ans.append(temp)
                else:
                    temp.reverse()
                    ans.append(temp)
                if flag:
                    flag=False
                else:
                    flag=True
                q.append(temp2)
        return ans
 {% endhighlight %}
