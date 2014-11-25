---
layout: post
title: First Missing Positive 
date: 2014-08-22 16:35:16
disqus: y
---

## 题意：
找出数组中第一个缺失的正整数

## 要求：
无

## 思路：
裸hash

##　更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        for(int i=0;i<n;i++)
            if(A[i]>0 && A[i]<n)
                if(A[i]-1!=i && A[i]!=A[A[i]-1])
                {
                    swap(A[i],A[A[i]-1]);
                    i--;
                }
        for(int i=0;i<n;i++)
            if(A[i]-1!=i)
                return i+1;
        return n+1;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if len(A)==0:
            return 1
        hash=[0 for i in range(10000)]
        for i in range(len(A)):
            if A[i]>0:
                hash[A[i]]=1
        for i in range(1,10000):
            if hash[i]==0:
                return i
 {% endhighlight %}
