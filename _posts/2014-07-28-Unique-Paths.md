---
layout: post
title: Unique Paths
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求从(1,1)点到(m,n)点的不同路径数，只能往右或往下走

## 要求：
无

## 思路：
组合数应用，共需要走m+n-2步，其中纵向n-1步，横向m-1步.

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int uniquePaths(int m, int n) {
        n-=1;
        m-=1;
        int dp[205][105];
        for(int i=0;i<=m+n;i++)
        {
            dp[i][0]=1;
        }
        for(int i=1;i<=m+n;i++)
        {
            for(int j=1;j<=i;j++)
            {
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1];
            }
        }
        return dp[m+n][m];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp=[[0 for i in range(105)] for j in range(205)]
        n-=1
        m-=1
        for i in range(m+n+1):
            dp[i][0]=1
        for i in range(1,m+n+1):
            for j in range(1,i+1):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        return dp[m+n][m]
 {% endhighlight %}
