---
layout: post
title: Best Time to Buy and Sell Stock III
date: 2014-08-22 10:00:16
disqus: y
---

## 题意：
还是卖股票，这次可以买卖两次

## 要求：


## 思路：
维护一个left和一个right数组，分别记录i天以前和以后的最大利润。

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int n=prices.size();
        int ans=0;
        if(n==0)
            return ans;
        vector<int> l(n,0);
        vector<int> r(n,0);
        int lastmin=prices[0];
        for(int i=1;i<n;i++)
        {
            lastmin=min(lastmin,prices[i]);
            l[i]=max(l[i-1],prices[i]-lastmin);
        }
        int lastmax=prices[n-1];
        for(int i=n-2;i>=0;i--)
        {
            lastmax=max(lastmax,prices[i]);
            r[i]=max(r[i+1],lastmax-prices[i]);
            ans=max(ans,l[i]+r[i]);
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        size = len(prices)
        if size==0:
            return 0
        l = [0 for x in range(size)]
        r = [0 for x in range(size)]
        minv = prices[0]
        for i in range(1,size):
            minv = min(minv,prices[i])
            l[i] = max(l[i-1],prices[i]-minv)
        maxv = prices[size-1]
        for i in range(size-2,-1,-1):
            maxv = max(maxv,prices[i])
            r[i] = max(r[i+1],maxv-prices[i])
        ans = 0
        for i in range(size):
            ans = max(ans,l[i]+r[i])
        return ans
 {% endhighlight %}
