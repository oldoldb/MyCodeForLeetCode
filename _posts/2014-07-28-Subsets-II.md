---
layout: post
title: Subsets II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求所有子集,原来的元素可能重复

## 要求：
无

## 思路：
递归深搜，加一个判重

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(int pos,int n,int start,vector<vector<int> >&ans,vector<int> &vec,vector<int> &S)
    {
        if(find(ans.begin(),ans.end(),vec)==ans.end())
        {
            ans.push_back(vec);
        }
        if(pos==n)
        {
            return ;
        }
        for(int i=start;i<n;i++)
        {
            vector<int> vec2(vec);
            vec2.push_back(S[i]);
            dfs(pos+1,n,i+1,ans,vec2,S);
            vec2.clear();
        }
    }
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        int n=S.size();
        sort(S.begin(),S.end());
        vector<vector<int> >ans;
        ans.clear();
        vector<int>vec;
        dfs(0,n,0,ans,vec,S);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    def dfs(self,pos,n,start,ans,vec,S):
        if ans.count(vec)==0:
            temp=vec[:]
            ans.append(temp)
        if pos==n:
            return 
        for i in range(start,n):
            vec2=vec[:]
            vec2.append(S[i])
            self.dfs(pos+1,n,i+1,ans,vec2,S)
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        ans=[]
        vec=[]
        self.dfs(0,len(S),0,ans,vec,S)
        return ans
 {% endhighlight %}
