---
layout: post
title: First Missing Positive 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
找出数组中第一个缺失的正整数

## 要求：
无

## 思路：
裸hash

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        int hash[10000]={0};
        for(int i=0;i<n;i++)
        {
            if(A[i]>0)
            {
                hash[A[i]]=1;
            }
        }
        for(int i=1;i<10000;i++)
        {
            if(hash[i]==0)
            {
                return i;
            }
        }
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
