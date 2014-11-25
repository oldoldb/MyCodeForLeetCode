---
layout: post
title: Median of Two Sorted Arrays
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
寻找两个有序数组合并后的中位数

## 要求：
时间复杂度O(log(n+m))

## 思路：
类似于二分的思想，实际上是寻找第K小，记得在豌豆荚三面的时候考过这个题。。。当时没有给出O（log(n+m))的
http://blog.csdn.net/zxzxy1988/article/details/8587244

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    double findKth(int A[],int m,int B[],int n,int k)
    {
        if(m>n)
        {
            return findKth(B,n,A,m,k);
        }
        if(m==0)
        {
            return B[k-1];
        }
        if(k==1)
        {
            return min(A[0],B[0]);
        }
        int pa=min(k/2,m);
        int pb=k-pa;
        if(A[pa-1]<B[pb-1])
        {
            return findKth(A+pa,m-pa,B,n,k-pa);
        }
        else if(A[pa-1]>B[pb-1])
        {
            return findKth(A,m,B+pb,n-pb,k-pb);
        }
        else
        {
            return A[pa-1];
        }
    }
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int total=m+n;
        if(total%2)
        {
            return findKth(A,m,B,n,total/2+1);
        }
        else
        {
            return (findKth(A,m,B,n,total/2)+findKth(A,m,B,n,total/2+1))/2;
        }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m=len(A)
        n=len(B)
        total=n+m
        if total%2==1:
            return self.findKth(A,m,B,n,total/2+1)
        else:
            return (self.findKth(A,m,B,n,total/2) + self.findKth(A,m,B,n,total/2+1))/2.0
    def findKth(self,A,m,B,n,k):
        if m>n:
            return self.findKth(B,n,A,m,k)
        if m==0:
            return B[k-1]
        if k==1:
            return min(A[0],B[0])
        pa=min(k/2,m)
        pb=k-pa
        if A[pa-1]<B[pb-1]:
            return self.findKth(A[pa:],m-pa,B,n,k-pa)
        elif A[pa-1]>B[pb-1]:
            return self.findKth(A,m,B[pb:],n-pb,k-pb)
        else:
            return A[pa-1]
 {% endhighlight %}
