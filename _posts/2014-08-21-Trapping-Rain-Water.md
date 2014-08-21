---
layout: post
title: Trapping Rain Water
date: 2014-08-21 17:27:16
disqus: y
---

## 题意：
n个整数代表n个阶梯的高度，求下雨后的积水量

## 要求：

## 思路：
先遍历一遍找到最高点
正反遍历一边，同时维护两边的次高点，对于低于次高点的点，可以存它们之间差的水量；如果高于次高点，那么更新次高点

## 更新：
总结leetcode堆栈题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int trap(int A[], int n) {
        int l=0;
        int r=n-1;
        int sum=0;
        int del=0;
        int curH=0;
        while(l<=r)
        {
            int minH=min(A[l],A[r]);
            if(minH>curH)
            {
                sum+=(minH-curH)*(r-l+1);
                curH=minH;
            }
            if(A[l]<A[r])
                del+=A[l++];
            else
                del+=A[r--];
        }
        return sum-del;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A)==0:
            return 0
        maxh=-1
        mark=0
        for i in range(len(A)):
            if A[i]>maxh:
                maxh=A[i]
                mark=i
        ans=0
        maxl=A[0]
        maxr=A[len(A)-1]
        for i in range(mark):
            if A[i]>maxl:
                maxl=A[i]
            else:
                ans+=maxl-A[i]
        for i in range(len(A)-1,mark,-1):
            if A[i]>maxr:
                maxr=A[i]
            else:
                ans+=maxr-A[i]
        return ans
 {% endhighlight %}
