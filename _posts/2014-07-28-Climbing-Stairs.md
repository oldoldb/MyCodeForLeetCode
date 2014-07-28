---
layout: post
title: Climbing Stairs
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
爬楼梯需要n步，每次可以爬1步或者2两步，求爬楼梯不同的方法数

## 要求：
无

## 思路：
显然递归，但是会RE，于是用dp来做，dp[i]表示爬i层的方法数,显然dp[1]=1,dp[2]=2,对于dp[i]，爬i层
- 一方面可以通过爬i-1层然后再爬1层，
- 或者通过爬i-2层再选择爬2层或者爬两个1层，但爬两个1层实际上就是dp[i-1]
所以dp[i]=dp[i-1]+dp[i-2]

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int climbStairs(int n) {
        int dp[1000];
        dp[1]=1;
        dp[2]=2;
        for(int i=3;i<=n;i++)
        {
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp=range(0,1000)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
 {% endhighlight %}
