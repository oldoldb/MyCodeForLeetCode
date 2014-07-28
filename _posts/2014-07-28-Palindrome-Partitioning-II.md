---
layout: post
title: Palindrome Partitioning II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求将字符串划分为回文子串，最小需要几刀

## 要求：


## 思路：
动态规划，预处理一个ok[i][j]，表示i~j是一个回文串，dp[i]表示0~i需要划分的刀数，则dp[i]=min(dp[i],dp[j-1]+1),j<i 并且s[i]==s[j-1]

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int minCut(string s) {
        int n=s.length();
        bool **ok=new bool*[n];
        for(int i=0;i<n;i++)
        {
            ok[i]=new bool[n];
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                ok[i][j]=false;
            }
        }
        int *dp=new int[n+1];
        for(int i=0;i<n;i++)
        {
            dp[i]=i+1;
        }
        for(int j=0;j<n;j++)
        {
            for(int i=j;i>=0;i--)
            {
                if(s[i]==s[j]&&(j-i<=1||ok[i+1][j-1]==true))
                {
                    ok[i][j]=true;
                    if(i>0)
                    {
                        dp[j]=min(dp[j],dp[i-1]+1);
                    }
                    else
                    {
                        dp[j]=min(dp[j],1);
                    }
                }
            }
        }
        return dp[n-1]-1;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n=len(s)
        ok=[[False for i in range(n)] for j in range(n)]
        dp=[i+1 for i in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if s[i]==s[j] and (j-i<=1 or ok[i+1][j-1]==True):
                    ok[i][j]=True
                    if i:
                        dp[j]=min(dp[j],dp[i-1]+1)
                    else:
                        dp[j]=min(dp[j],1)
        return dp[n-1]-1
 {% endhighlight %}
