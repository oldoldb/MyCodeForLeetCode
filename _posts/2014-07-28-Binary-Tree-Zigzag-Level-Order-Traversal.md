---
layout: post
title: Binary Tree Zigzag Level Order Traversal
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
按Zigzag次序按层次遍历树

## 要求：


## 思路：
同普通的按层次遍历树，加一个是否reverse标记就好

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
        if(root==NULL)
        {
            return ans;
        }
        queue<vector<TreeNode*> >q;
        vector<TreeNode*>s;
        s.push_back(root);
        q.push(s);
        bool flag=true;
        while(!q.empty())
        {
            s=q.front();
            q.pop();
            vector<int>temp;
            vector<TreeNode*>temp2;
            for(vector<TreeNode *>::iterator it=s.begin();it!=s.end();it++)
            {
                temp.push_back((*it)->val);
                if((*it)->left!=NULL)
                {
                    temp2.push_back((*it)->left);
                }
                if((*it)->right!=NULL)
                {
                    temp2.push_back((*it)->right);
                }
            }
            if(temp.size())
            {
                if(flag)
                {
                    ans.push_back(temp);
                }
                else
                {
                    reverse(temp.begin(),temp.end());
                    ans.push_back(temp);
                }
                q.push(temp2);
                flag=!flag;
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
