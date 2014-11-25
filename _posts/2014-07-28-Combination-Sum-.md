---
layout: post
title: Combination Sum 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给定一组数和一个目标值，找出所有组合使和为T，可以重复

## 要求：
无

## 思路：
深搜

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(vector<int> &candidates,int target,int pos,vector<int> &vec,vector<vector<int> >&ans)
    {
        if(target==0)
        {
            ans.push_back(vec);
            return ;
        }
        for(int i=pos;i<candidates.size();i++)
        {
            if(target<candidates[i])
            {
                return ;
            }
            vec.push_back(candidates[i]);
            dfs(candidates,target-candidates[i],i,vec,ans);
            vec.pop_back();
        }
    }
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<vector<int> >ans;
        vector<int>vec;
        dfs(candidates,target,0,vec,ans);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    def dfs(self,candidates,target,pos,vec,ans):
        if target==0:
            vec2=vec[:]
            ans.append(vec2)
            return 
        for i in range(pos,len(candidates)):
            if target<candidates[i]:
                return 
            vec.append(candidates[i])
            self.dfs(candidates,target-candidates[i],i,vec,ans)
            vec.pop()
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        vec=[]
        ans=[]
        self.dfs(candidates,target,0,vec,ans)
        return ans
 {% endhighlight %}
