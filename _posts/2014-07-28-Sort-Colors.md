---
layout: post
title: Sort Colors
date: 2014-08-22 16:56:16
disqus: y
---

## 题意：
将只含0、1、2的数组排序

## 要求：
不能用库排序函数
只扫描一遍

## 思路：
设置三个指针p0,p1,p2分别指向0,1,2的位置
遍历p1的位置
- A[p1]==0:swap[A[p1],A[p0]),同时p0,p1分别指向下一个位置
- A[p1]==1:p1指向下一个位置
- A[p1]==2:swap(A[p1],A[p2]),同时p2指向前一个位置

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void sortColors(int A[], int n) {
        int p0=0;
        int p1=0;
        int p2=n-1;
        while(p1<=p2)
            if(A[p1]==0)
            {
                swap(A[p0],A[p1]);
                p0++;
                p1++;
            }
            else if(A[p1]==1)
                p1++;
            else
            {
                swap(A[p1],A[p2]);
                p2--;
            }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        p0=0
        p1=0
        p2=len(A)-1
        while p1<=p2:
            if A[p1]==0:
                A[p1],A[p0]=A[p0],A[p1]
                p0+=1
                p1+=1
            elif A[p1]==1:
                p1+=1
            else:
                A[p1],A[p2]=A[p2],A[p1]
                p2-=1
        
 {% endhighlight %}
