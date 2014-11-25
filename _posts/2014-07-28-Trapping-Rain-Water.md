---
layout: post
title: Trapping Rain Water
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
n个整数代表n个阶梯的高度，求下雨后的积水量

## 要求：

## 思路：
先遍历一遍找到最高点
正反遍历一边，同时维护两边的次高点，对于低于次高点的点，可以存它们之间差的水量；如果高于次高点，那么更新次高点

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int trap(int A[], int n) {
        int maxh=-1;
        int maxl=A[0];
        int maxr=A[n-1];
        int mark=0;
        for(int i=0;i<n;i++)
        {
            if(A[i]>maxh)
            {
                maxh=A[i];
                mark=i;
            }
        }
        int ans=0;
        for(int i=0;i<mark;i++)
        {
            if(A[i]>maxl)
            {
                maxl=A[i];
            }
            else
            {
                ans+=maxl-A[i];
            }
        }
        for(int i=n-1;i>mark;i--)
        {
            if(A[i]>maxr)
            {
                maxr=A[i];
            }
            else
            {
                ans+=maxr-A[i];
            }
        }
        return ans;
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
