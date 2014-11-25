---
layout: post
title: Palindrome Partitioning
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求字符串划分为回文子串的所有划分方式

## 要求：


## 思路：
des深搜，同时事先预处理一个dp[i][j]数组，dp[i][j]=1表示i~j区间为回文串，深搜的时候维护一个mark[i]数组，mark[i]=1表示从i点划分

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(int pos,string s,vector<vector<string> >&ans,int **dp,vector<int> &mark)
    {
        if(pos==s.length())
        {
            vector<string> vec;
            string str="";
            for(int i=0;i<s.length();i++)
            {
                str+=s[i];
                if(mark[i])
                {
                    vec.push_back(str);
                    str="";
                }
            }
            ans.push_back(vec);
            return ;
        }
        for(int i=pos;i<s.length();i++)
        {
            if(dp[pos][i]==1)
            {
                mark[i]=1;
                dfs(i+1,s,ans,dp,mark);
                mark[i]=0;
            }
        }
    }
    vector<vector<string>> partition(string s) {
        int n=s.length();
        int **dp=new int*[n];
        for(int i=0;i<n;i++)
        {
            dp[i]=new int[n];
        }
        vector<vector<string> >ans;
        vector<int>mark;
        mark.resize(n);
        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n;j++)
            {
                bool flag=true;
                for(int k=0;k<(j-i+1)/2;k++)
                {
                    if(s[i+k]!=s[j-k])
                    {
                        flag=false;
                        break;
                    }
                }
                if(flag)
                {
                    dp[i][j]=1;
                }
                else
                {
                    dp[i][j]=0;
                }
            }
        }
        dfs(0,s,ans,dp,mark);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    def dfs(self,pos,vec,ans,s,dp):
        if pos==len(s):
            ans.append(vec)
            return 
        for i in range(pos,len(s)):
            if dp[pos][i]==True:
                self.dfs(i+1,vec[:]+[s[pos:i+1]],ans,s,dp)
                
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        ans=[]
        n=len(s)
        dp=[[False for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i,-1,-1):
                if s[i]==s[j] and (i-j<=1 or dp[j+1][i-1]==True):
                    dp[j][i]=True
        self.dfs(0,[],ans,s,dp)
        return ans
 {% endhighlight %}
