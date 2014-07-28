---
layout: post
title: Search in Rotated Sorted Array II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
在根据某个点旋转后的有序数组中(元素可以重复）查找指定元素的下标

## 要求：

## 思路：
二分算法，但是目前不会写
这道题数据太水，试着交了一发O(n)竟然也给过

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool search(int A[], int n, int target) {
        for(int i=0;i<n;i++)
        {
            if(A[i]==target)
            {
                return true;
            }
        }
        return false;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        for i in range(len(A)):
            if A[i]==target:
                return True
        return False
 {% endhighlight %}
