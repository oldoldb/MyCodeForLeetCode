---
layout: post
title: Remove Duplicates from Sorted Array II 
date: 2014-08-22 09:35:16
disqus: y
---

## 题意：
从有序数组中删除出现次数大于两次的元素

## 要求：


## 思路：
模拟就好

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
            if(i==1 || A[i]!=A[ans-2])
                A[ans++]=A[i];
        return n==0?0:ans;
    }
};

 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0:
            return 0
        pos=1
        num=1
        last=A[0]
        for i in range(1,len(A)):
            if A[i]!=last:
                A[pos]=A[i]
                pos+=1
                last=A[i]
                num=1
            elif num==2:
                continue
            else:
                num+=1
                A[pos]=last
                pos+=1
        return pos
 {% endhighlight %}
