---
layout: post
title: Divide Two Integers
date: 2014-08-23 13:09:16
disqus: y
---

## 题意：
模拟除法

## 要求：


## 思路：
用二分的思想
http://blog.csdn.net/pickless/article/details/9150617
http://www.cnblogs.com/lihaozy/archive/2012/12/30/2840070.html

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int divide(int dividend, int divisor) {
        long long ndividend=abs((long long)dividend);
        long long ndivisor=abs((long long)divisor);
        long long ans=0;
        while(ndividend>=ndivisor)
        {
            long long temp=ndivisor;
            for(int i=0;ndividend>=temp;i++,temp<<=1)
            {
                ndividend-=temp;
                ans+=1<<i;
            }
        }
        if(dividend>0 && divisor>0 || dividend<0 && divisor<0)
            return ans;
        else
            return -ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend==0 or divisor==0:
            return 0
        flag=0
        if dividend>0 and divisor<0 or dividend<0 and divisor>0:
            flag=1
        c=dividend
        d=divisor
        a=abs(c)
        b=abs(d)
        if b>a:
            return 0
        sum=0
        cnt=0
        ans=0
        while b<=a:
            cnt=1
            sum=b
            while sum+sum<=a:
                sum+=sum
                cnt+=cnt
            a-=sum
            ans+=cnt
        if flag:
            ans=-ans
        return ans
 {% endhighlight %}
