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

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int findMin(vector<int> &num) {
        int n=num.size();
        int r=n-1;
        int l=0;
        int m=0;
        if(num[l]<=num[r])
            return num[l];
        while(l<=r)
        {
            m=l+(r-l)/2;
            if(m<n-1 && num[m+1]<num[m])
                return num[m+1];
            if(m>0 && num[m]<num[m-1])
                return num[m];
            if(num[r]>num[m])
                r=m-1;
            else
                l=m+1;
        }
        return num[m];
    }
};
 {% endhighlight %}

