---
layout: post
title: Search for a Range
date: 2014-08-23 14:18:16
disqus: y
---

## 题意：
求有序数组中指定元素的范围

## 要求：
时间复杂度O(logn)

## 思路：
二分，当target==A[m]的时候，判断A[m]与相邻元素的关系，缩小二分范围

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<int> searchRange(int A[], int n, int target) {
        vector<int> ans;
        int ansl=-1;
        int ansr=-1;
        int l=0;
        int r=n-1;
        while(l<=r)
        {
            int m=l+(r-l)/2;
            if(A[m]==target)
            {
                if(m==0)
                {
                    ansl=0;
                    break;
                }
                else if(A[m]==A[m-1])
                {
                    l=0;
                    r=m-1;
                }
                else
                {
                    ansl=m;
                    break;
                }
            }
            else if(A[m]<target)
                l=m+1;
            else
                r=m-1;
        }
        l=0;
        r=n-1;
        while(l<=r)
        {
            int m=l+(r-l)/2;
            if(A[m]==target)
            {
                if(m==n-1)
                {
                    ansr=n-1;
                    break;
                }
                else if(A[m]==A[m+1])
                {
                    l=m+1;
                    r=n;
                }
                else
                {
                    ansr=m;
                    break;
                }
            }
            else if(A[m]<target)
                l=m+1;
            else
                r=m-1;
        }
        ans.push_back(ansl);
        ans.push_back(ansr);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        ans=[]
        n=len(A)-1
        ansl=-1
        ansr=-1
        if A==None:
            ans.append(ansl)
            ans.append(ansr)
            return ans
        l=0
        r=n
        while l<=r:
            m=l+(r-l)/2
            if A[m]==target:
                if m==0:
                    ansl=0
                    break
                elif A[m]==A[m-1]:
                    l=0
                    r=m-1
                else:
                    ansl=m
                    break
            elif A[m]<target:
                l=m+1
            else:
                r=m-1
        ans.append(ansl)
        
        l=0
        r=n
        while l<=r:
            m=l+(r-l)/2
            if A[m]==target:
                if m==n:
                    ansr=n
                    break
                elif A[m]==A[m+1]:
                    l=m+1
                    r=n
                else:
                    ansr=m
                    break
            elif A[m]<target:
                l=m+1
            else:
                r=m-1
        ans.append(ansr)
        return ans
 {% endhighlight %}
