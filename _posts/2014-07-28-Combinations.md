---
layout: post
title: Combinations
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求组合Cnk

## 要求：
无

## 思路：
递归

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(int pos,int k,int n,int start,vector<vector<int> > &ans,vector<int> &vec)
    {
        if(pos==k)
        {
            ans.push_back(vec);
            return ;
        }
        for(int i=start;i<=n;i++)
        {
            vec[pos]=i;
            dfs(pos+1,k,n,i+1,ans,vec);
        }
    }
    vector<vector<int> > combine(int n, int k) {
        vector<vector<int> >ans;
        ans.clear();
        vector<int>vec;
        vec.resize(k);
        dfs(0,k,n,1,ans,vec);
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
