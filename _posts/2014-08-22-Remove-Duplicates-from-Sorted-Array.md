---
layout: post
title: Remove Duplicates from Sorted Array
date: 2014-08-22 09:31:16
disqus: y
---

## 题意：
在一个有序数组中删除重复的数

## 要求：
原地删除

## 思路：
由于是有序的，所以遍历数组，判断当前元素A[i]与last
- A[i]==last,跳过
- A[i]!=last,用last更新A[pos],同时Pos++，更新last

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int ans=1;
        for(int i=1;i<n;i++)
            if(A[i]!=A[ans-1])
                A[ans++]=A[i];
        return n==0?0:ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0:
            return 0
        last=A[0]
        pos=0
        for i in range(len(A)):
            if last!=A[i]:
                A[pos]=last
                pos+=1
                last=A[i]
        A[pos]=last
        pos+=1
        return pos
 {% endhighlight %}
