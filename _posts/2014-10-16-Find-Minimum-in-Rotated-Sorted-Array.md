---
layout: post
title: Find Minimum in Rotated Sorted Array
date: 2014-10-16 12:24:16
disqus: y
---

## 题意：
旋转数组中寻找最小值

## 要求：


## 思路：
最小值一定满足小于左右的数，二分查找
https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int findMin(vector<int> &num) {
        int l=0;
        int r=num.size()-1;
        while(l<r && num[l]>=num[r])
        {
            int m=l+(r-l)/2;
            if(num[m]>num[r])
                l=m+1;
            else
                r=m;
        }
        return num[l];
    }
};
 {% endhighlight %}

