---
layout: post
title: Search in Rotated Sorted Array
date: 2014-08-22 12:39:16
disqus: y
---

## 题意：
在根据某个点旋转后的有序数组中查找指定元素的下标

## 要求：

## 思路：
二分算法，但是目前不会写
这道题数据太水，试着交了一发O(n)竟然也给过

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int search(int A[], int n, int target) {
        int l=0;
        int r=n-1;
        while(l<=r)
        {
            int m=l+(r-l)/2;
            if(A[m]==target)
                return m;
            else if(A[l]<A[m])
                if(A[l]<=target && target<A[m])
                    r=m-1;
                else
                    l=m+1;
            else if(A[l]>A[m])
                if(A[m]<target && target<=A[r])
                    l=m+1;
                else
                    r=m-1;
            else
                l++;
        }
        return -1;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        for i in range(len(A)):
            if A[i]==target:
                return i
        return -1
 {% endhighlight %}
