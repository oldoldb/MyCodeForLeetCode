---
layout: post
title: Best Time to Buy and Sell Stock II 
date: 2014-08-22 09:52:16
disqus: y
---

## 题意：
数组表示每天股票的价格，设计算法求最大利润。可以进行多次股票交易，但在买入新股票之前必须将旧股票卖出

## 要求：
无

## 思路：
考虑a[i],a[i+1],a[i+2]，如果a[i+2]>a[i+1]>a[i]，那么下面两种情况：
- i天买入，i+1天不买，i+2天买入，利润a[i+2]-a[i]
- i天买入，i+1天卖出，同时i+1天买入，i+2天卖出，利润a[i+1]-a[i]+a[i+2]-a[i+1]=a[i+2]-a[i]
两只情况实际是一致的。
所以每当递增序列出现时，就累加到利润上就好

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int ans=0;
        for(int i=0;i<prices.size();i++)
            if(i>0 && prices[i]>prices[i-1])
                ans+=prices[i]-prices[i-1];
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
        last=10000
        ans=0
        for i in range(len(prices)):
            if prices[i]>last:
                ans+=prices[i]-last
            last=prices[i]
        return ans
 {% endhighlight %}
