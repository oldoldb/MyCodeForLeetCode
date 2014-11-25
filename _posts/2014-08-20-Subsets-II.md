---
layout: post
title: Subsets II
date: 2014-08-20 20:39:16
disqus: y
---

## 题意：
求所有子集,原来的元素可能重复

## 要求：
无

## 思路：
递归深搜，加一个判重

## 更新：
总结leetcode排列组合题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        sort(S.begin(),S.end());
        vector<vector<int> > ans(1);
        int last=S[0];
        int lastIndex=0;
        for(int i=0;i<S.size();i++)
        {
            int temp=lastIndex;
            if(S[i]!=last)
            {
                last=S[i];
                temp=0;
            }
            int n=ans.size();
            lastIndex=n;
            for(int j=n-1;j>=temp;j--)
            {
                ans.push_back(ans[j]);
                ans.back().push_back(S[i]);
            }
        }
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
