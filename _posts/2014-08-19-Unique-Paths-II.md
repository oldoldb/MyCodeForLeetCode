---
layout: post
title: Unique Paths II
date: 2014-08-19 16:55:16
disqus: y
---

## 题意：
求(0,0)点到(n,m)点的路径数，可能有不可走的地方，只能向右向下走

## 要求：
无

## 思路：
基本的dp，如果当前格子不可走,dp[i][j]=0，否则dp[i][j]=dp[i-1][j]+dp[i][j-1]

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int n=obstacleGrid.size();
        int m=obstacleGrid[0].size();
        int *dp=new int[max(n,m)+1];
        dp[0]=!obstacleGrid[0][0];
        for(int i=1;i<m;i++)
            if(dp[i-1]==0 || obstacleGrid[0][i]==1)
                dp[i]=0;
            else
                dp[i]=dp[i-1];
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(obstacleGrid[i][j]==0)
                {
                    if(j>0)
                        dp[j]=dp[j-1]+dp[j];
                }
                else
                    dp[j]=0;
            }
        }
        return dp[m-1];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0 for i in range(105)] for j in range(205)]
        if obstacleGrid[0][0]==1:
            dp[0][0]=0
        else:
            dp[0][0]=1
        for i in range(1,n):
            if obstacleGrid[i][0]==1:
                dp[i][0]=0
            else:
                dp[i][0]=dp[i-1][0]
        for j in range(1,m):
            if obstacleGrid[0][j]==1:
                dp[0][j]=0
            else:
                dp[0][j]=dp[0][j-1]
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
 {% endhighlight %}
