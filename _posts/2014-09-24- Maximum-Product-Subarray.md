---
layout: post
title: Maximum Product Subarray
date: 2014-09-24 14:37:16
disqus: y
---

## 题意：
最大子数组的变形，求最大子数组的积

## 要求：


## 思路：
最大积可能是正数 * 正数，也可能是负数 * 负数，遍历的时候分别保存最大积和最小积。

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxProduct(int A[], int n) {
        if(n==0)
            return 0;
        int ans=A[0];
        int ansmax=A[0];
        int ansmin=A[0];
        for(int i=1;i<n;i++)
        {
            int tempmax=ansmax;
            int tempmin=ansmin;
            ansmax=max(max(tempmax*A[i],tempmin*A[i]),A[i]);
            ansmin=min(min(tempmax*A[i],tempmin*A[i]),A[i]);
            ans=max(ans,ansmax);
        }
        return ans;
    }
};
 {% endhighlight %}

