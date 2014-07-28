---
layout: post
title: Best Time to Buy and Sell Stock
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
数组元素代表每天股票的价格，求最大利润（至多买卖一次）

## 要求：
无

## 思路：
即求数组最大元素差（后-前），那么只要遍历一边数组，维护一个最大差，如果当前元素比前面的最小元素还要小，就更新最小元素

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if(prices.size()==0)
        {
            return 0;
        }
        int ans=0;
        int lastmin=prices[0];
        for(vector<int>::iterator it=prices.begin();it!=prices.end();it++)
        {
            if(*it>lastmin)
            {
                ans=max(ans,*it-lastmin);
            }
            else
            {
                lastmin=*it;
            }
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
        if len(prices)==0:
            return 0
        ans=0
        lastmin=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>lastmin:
                ans=max(ans,prices[i]-lastmin)
            else:
                lastmin=prices[i]
        return ans
 {% endhighlight %}
