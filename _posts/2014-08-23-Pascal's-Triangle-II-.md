---
layout: post
title: Pascal's Triangle II 
date: 2014-08-23 09:57:16
disqus: y
---

## 题意：
求Pascal’s Triangle的第k行

## 要求：
O(k)空间复杂度

## 思路：
记ans[i]位第任意一行第i个值，那么容易知道扫到某一行时，ans[i]记录的是上一行i位置的值，ans[i]=ans[i]+ans[i-1]，为了不让ans[i-1]先改变，可以从后往前扫

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans(rowIndex+1,0);
        ans[0]=1;
        for(int i=1;i<=rowIndex;i++)
            for(int j=i;j>=1;j--)
                ans[j]+=ans[j-1];
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        ans=[[] for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i,-1,-1):
                if j==0:
                    ans[j]=1
                elif j==i:
                    ans[j]=ans[j-1]
                else:
                    ans[j]=ans[j]+ans[j-1]
        return ans
 {% endhighlight %}
