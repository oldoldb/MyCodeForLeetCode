---
layout: post
title: Remove Element
date: 2014-08-22 09:16:16
disqus: y
---

## 题意：
给一个数组和一个目标元素，删除所有和目标元素相同的元素，返回删除后的数组长度（数组元素顺序可以改变）

## 要求：
无

## 思路：
遍历数组，每次找到和目标元素相同的元素，就把它和最后一个元素交换，同时数组长度n-1，最后返回n就好

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int ans=0;
        for(int i=0;i<n;i++)
            if(A[i]!=elem)
                A[ans++]=A[i];
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n=len(A)
        i=0
        while i!=n:
            if A[i]==elem:
                A[i],A[n-1]=A[n-1],A[i]
                i=i-1
                n=n-1
            i=i+1
        return n
        
 {% endhighlight %}
