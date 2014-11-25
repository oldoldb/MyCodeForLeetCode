---
layout: post
title: Merge Sorted Array
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
合并有序数组

## 要求：
无

## 思路：


## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int *C=new int[m];
        for(int i=0;i<m;i++)
        {
            C[i]=A[i];
        }
        int posA=0;
        int posB=0;
        while(posA<m&&posB<n)
        {
            if(C[posA]<B[posB])
            {
                A[posA+posB]=C[posA];
                posA++;
            }
            else
            {
                A[posA+posB]=B[posB];
                posB++;
            }
        }
        while(posA<m)
        {
            A[posA+posB]=C[posA];
            posA++;
        }
        while(posB<n)
        {
            A[posA+posB]=B[posB];
            posB++;
        }
        return ;
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
