---
layout: post
title: Remove Duplicates from Sorted Array
date: 2014-07-28 15:52:16
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

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if(n==0)
        {
            return 0;
        }
        int pos=0;
        int last=A[0];
        for(int i=0;i<n;i++)
        {
            if(A[i]!=last)
            {
                A[pos++]=last;
                last=A[i];
            }
        }
        A[pos++]=last;
        return pos;
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
