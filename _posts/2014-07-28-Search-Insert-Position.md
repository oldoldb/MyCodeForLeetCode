---
layout: post
title: Search Insert Position
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给一个有序数组和一个目标元素，如果该目标元素在数组中，就返回下标值；如果不在数组中，就返回合适的插入位置，使数组仍然有序

## 要求：
无

## 思路：
依照题意，sorted array应该是升序数组的意思（否则对于只有一个元素的情况无法判断），那么遍历数组，只要目标元素<=A[i]，就返回i就好;如果遍历完没有找到合适位置，就返回最后一个位置n就好

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int searchInsert(int A[], int n, int target) {
        for(int i=0;i<n;i++)
        {
            if(target<=A[i])
            {
                return i;
            }
        }
        return n;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if target<=A[i]:
                return i
        return len(A)

 {% endhighlight %}
