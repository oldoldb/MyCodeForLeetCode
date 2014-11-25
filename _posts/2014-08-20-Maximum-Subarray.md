---
layout: post
title: Maximum Subarray
date: 2014-08-20 14:19:16
disqus: y
---

## 题意：
求数组的最大连续子数组（至少含有一个元素）

## 要求：
找到O(n)算法之后，再写一个分治算法

## 思路：
记dp[i]位以i结尾的前i个数的最大子数组，那么对于dp[i]
- 如果dp[i-1]+A[i]>A[i],即dp[i-1]>0，显然dp[i]=dp[i-1]+A[i]
- 如果dp[i-1]+A[i]<A[i],即dp[i-1]<0，显然dp[i]=A[i]
对于dp[i-1]=0的情况放在哪里都可以
同时由于dp[i]只和dp[i-1]有关系，所以不需要开一个数组，而只用一个temp来记录即可
扫一遍数组，ans=max{dp[i]}
对于分治思想，还没有想出来，以后再补充

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxSubArrayHelper(int A[],int l,int r)
    {
        if(l>=r)
            return A[l];
        int m=l+(r-l)/2;
        int left=maxSubArrayHelper(A,l,m);
        int right=maxSubArrayHelper(A,m+1,r);
        int lmax=A[m];
        int temp=0;
        for(int i=m;i>=l;i--)
        {
            temp+=A[i];
            lmax=max(lmax,temp);
        }
        temp=0;
        int rmax=A[m+1];
        for(int i=m+1;i<=r;i++)
        {
            temp+=A[i];
            rmax=max(rmax,temp);
        }
        return max(max(left,right),lmax+rmax);
    }
    int maxSubArray(int A[], int n) {
        return maxSubArrayHelper(A,0,n-1);
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        tempans=A[0]
        ans=A[0]
        for i in range(1,len(A)):
            if tempans>0:
                tempans+=A[i]
            else:
                tempans=A[i]
            ans=max(ans,tempans)
        return ans
 {% endhighlight %}
