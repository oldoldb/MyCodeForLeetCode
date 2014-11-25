---
layout: post
title: Merge Sorted Array
date: 2014-08-22 13:28:16
disqus: y
---

## 题意：
合并有序数组

## 要求：
无

## 思路：

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        for(int i=m+n-1;i>=0;i--)
            if(m<=0)
                A[i]=B[--n];
            else if(n<=0)
                break;
            else if(A[m-1]<B[n-1])
                A[i]=B[--n];
            else
                A[i]=A[--m];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        C=A[:]
        posA=0
        posB=0
        while posA<m and posB<n:
            if C[posA]<B[posB]:
                A[posA+posB]=C[posA]
                posA+=1
            else:
                A[posA+posB]=B[posB]
                posB+=1
        while posA<m:
            A[posA+posB]=C[posA]
            posA+=1
        while posB<n:
            A[posA+posB]=B[posB]
            posB+=1
 {% endhighlight %}
