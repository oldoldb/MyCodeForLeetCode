---
layout: post
title: Jump Game II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
数组中每个元素代表所能跳的最大距离，问从0出发到达终点最少需要几跳

## 要求：


## 思路：
O(n^2)的dp会TLE
每次记录最远能够到达的范围，每次都在此范围内搜，找到下一跳的最远范围，更新最远范围和跳数

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int jump(int A[], int n) {
        if(n==1)
        {
            return 0;
        }
        int ans=0;
        int maxdis=0;
        while(true)
        {
            ans++;
            int temp=maxdis;
            for(int i=0;i<=temp;i++)
            {
                maxdis=max(maxdis,i+A[i]);
                if(maxdis>=n-1)
                {
                    return ans;
                }
            }
        }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n=len(A)
        if n==1:
            return 0
        maxdis=0
        ans=0
        while True:
            ans+=1
            for i in range(maxdis+1):
                maxdis=max(maxdis,A[i]+i)
                if maxdis>=n-1:
                    return ans
 {% endhighlight %}
