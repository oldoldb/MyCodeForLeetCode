---
layout: post
title: Find Minimum in Rotated Sorted Array II
date: 2014-10-22 09:17:16
disqus: y
---

## 题意：
旋转数组中寻找最小值

## 要求：
数组中可能有重复元素

## 思路：
最小值一定满足小于左右的数，二分查找

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
            else if(num[m]<num[r])
                r=m;
            else
                l=l+1;
        }
        return num[l];
    }
};
 {% endhighlight %}

