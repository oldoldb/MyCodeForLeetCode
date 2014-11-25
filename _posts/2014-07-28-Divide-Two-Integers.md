---
layout: post
title: Divide Two Integers
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
模拟除法

## 要求：


## 思路：
用二分的思想
http://blog.csdn.net/pickless/article/details/9150617
http://www.cnblogs.com/lihaozy/archive/2012/12/30/2840070.html

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    long long add(long long p,long long num)
    {
        if(p==0)
        {
            return 0;
        }
        long long temp=add(p>>1,num)<<1;
        if((p&1)!=0)
        {
            temp+=num;
        }
        return temp;
    }
    int divide(int dividend, int divisor) {
        int flag=1;
        int ans=0;
        if((dividend<0 && divisor>0) || (dividend>0 && divisor<0))
        {
            flag=-1;
        }
        long long ndividend = abs((long long) dividend);
        long long ndivisor = abs((long long)divisor);
        long long l=0;
        long long r=ndividend;
        while(l<=r)
        {
            long long m=(l+r)>>1;
            long long temp=add(m,ndivisor);
            if(temp==ndividend)
            {
                ans=m;
                break;
            }
            else if(temp<ndividend)
            {
                ans=m;
                l=m+1;
            }
            else
            {
                r=m-1;
            }
        }
        return flag<0?-ans:ans;
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
