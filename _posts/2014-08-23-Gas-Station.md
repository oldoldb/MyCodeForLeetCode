---
layout: post
title: Gas Station
date: 2014-08-23 14:16:16
disqus: y
---

## 题意：
沿环有N个加油站，每个站可以提供gas[i],车的邮箱从i到i+1需要消耗cost[i]的油，问从何处开始可以绕圈完成

## 要求：


## 思路：
假设从i走到j时，刚好油不够，那么i~j之间的加油站都不能作为起点（想想就可以了）
所以从j+1开始继续判断

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int sum=0;
        int total=0;
        int start=0;
        for(int i=0;i<gas.size();i++)
        {
            sum+=gas[i]-cost[i];
            total+=gas[i]-cost[i];
            if(sum<0)
            {
                start=(i+1)%gas.size();
                sum=0;
            }
        }
        return total<0?-1:start;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        sum=0
        total=0
        start=0
        for i in range(len(gas)):
            sum+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if sum<0:
                start=(i+1)%len(gas)
                sum=0
        if total<0:
            return -1
        else:
            return start
 {% endhighlight %}
