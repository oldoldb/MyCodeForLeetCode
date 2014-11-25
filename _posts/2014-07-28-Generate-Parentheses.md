---
layout: post
title: Generate Parentheses
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给定n，生成n个括号所有合法序列

## 要求：


## 思路：
深搜

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(int lpos,int rpos,int n,vector<string> &ans,string str)
    {
        if(rpos>lpos || lpos>n && rpos>n)
        {
            return ;
        }
        if(lpos==n && rpos==n)
        {
            ans.push_back(str);
            return ;
        }
        if(lpos<n)
        {
            string temp=str;
            temp+='(';
            dfs(lpos+1,rpos,n,ans,temp);
        }
        if(rpos<n)
        {
            string temp=str;
            temp+=')';
            dfs(lpos,rpos+1,n,ans,temp);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string>ans;
        if(n==0)
        {
            return ans;
        }
        string str="";
        dfs(0,0,n,ans,str);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    def dfs(self,lpos,rpos,n,ans,str):
        if rpos>lpos or lpos>n and rpos>n:
            return 
        if lpos==n and rpos==n:
            ans.append(str)
            return 
        if lpos<n:
            temp=str[:]
            temp+='('
            self.dfs(lpos+1,rpos,n,ans,temp)
        if rpos<n:
            temp=str[:]
            temp+=')'
            self.dfs(lpos,rpos+1,n,ans,temp)
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ans=[]
        str=""
        self.dfs(0,0,n,ans,str)
        return ans
 {% endhighlight %}
