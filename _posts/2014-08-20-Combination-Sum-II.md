---
layout: post
title: Combination Sum II
date: 2014-08-20 10:48:16
disqus: y
---

## 题意：
给定一组数和一个目标值，找出所有组合使和为T，不可以重复

## 要求：
无

## 思路：
排序，深搜，每次搜的时候判断一下是否和上一个数重复

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(vector<vector<int> > &ans,vector<int> vec,vector<int> num,int target,int pos)
    {
        if(target==0)
        {
            ans.push_back(vec);
            return ;
        }
        int last=-1;
        for(int i=pos;i<num.size();i++)
        {
            if(num[i]==last)
                continue;
            if(target<num[i])
                return;
            last=num[i];
            vec.push_back(num[i]);
            dfs(ans,vec,num,target-num[i],i+1);
            vec.pop_back();
        }
    }
    vector<vector<int> > combinationSum2(vector<int> &num, int target) {
        sort(num.begin(),num.end());
        vector<vector<int> > ans;
        vector<int> vec;
        dfs(ans,vec,num,target,0);
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
        last=-1
        for i in range(pos,len(candidates)):
            if last==candidates[i]:
                continue
            if target<candidates[i]:
                return 
            last=candidates[i]
            vec.append(candidates[i])
            self.dfs(candidates,target-candidates[i],i+1,vec,ans)
            vec.pop()
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        vec=[]
        ans=[]
        self.dfs(candidates,target,0,vec,ans)
        return ans
 {% endhighlight %}
