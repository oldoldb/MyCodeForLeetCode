---
layout: post
title: Minimum Path Sum
date: 2014-08-20 10:40:16
disqus: y
---

## 题意：
m*n矩阵，求从(0,0)点到(m-1,n-1)点的最小路径和，只能向右向下走

## 要求：


## 思路：
很基本的dp，dp[i][j]=max(dp[i-1][j],dp[i][j-1])+A[i][j]

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int minPathSum(vector<vector<int> > &grid) {
        int n=grid.size();
        int m=grid[0].size();
        vector<int>dp(m+1,INT_MAX);
        dp[1]=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                dp[j+1]=min(dp[j],dp[j+1])+grid[i][j];
            }
        }
        return dp[m];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
 {% endhighlight %}
