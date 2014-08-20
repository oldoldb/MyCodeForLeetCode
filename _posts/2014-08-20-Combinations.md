---
layout: post
title: Combinations
date: 2014-08-20 19:50:16
disqus: y
---

## 题意：
求组合Cnk

## 要求：
无

## 思路：
递归

## 更新：
总结leetcode排列组合题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(vector<vector<int> > &ans,vector<int> vec,int n,int k,int pos,int start)
    {
        if(pos==k)
        {
            ans.push_back(vec);
            return ;
        }
        for(int i=start;i<=n;i++)
        {
            vec[pos]=i;
            dfs(ans,vec,n,k,pos+1,i+1);
        }
    }
    vector<vector<int> > combine(int n, int k) {
        vector<vector<int> >ans;
        vector<int>vec(k);
        dfs(ans,vec,n,k,0,1);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    def dfs(self,pos,k,n,start,ans,vec):
        if pos==k:
            temp=vec[:]
            ans.append(temp)
            return 
        for i in range(start,n+1):
            vec[pos]=i
            self.dfs(pos+1,k,n,i+1,ans,vec)
    # @return a list of lists of integers
    def combine(self, n, k):
        ans=[]
        vec=[0 for i in range(k)]
        self.dfs(0,k,n,1,ans,vec)
        return ans
        
 {% endhighlight %}
