---
layout: post
title: Search a 2D Matrix
date: 2014-08-22 10:52:16
disqus: y
---

## 题意：
在一个按行按列有序的二维矩阵中寻找目标元素

## 要求：
无

## 思路：
每次都比较矩阵右上角的点，记为A[row][col]
- A[row][col]==target,目标元素找到
- A[row][col]>target,则目标元素不可能出现在col列，继续比较A[row][col-1]
- A[row][col]<target,则目标元素不可能出现在row列，继续比较A[row+1][col]

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int n=matrix.size();
        int m=matrix[0].size();
        int l=0;
        int r=n-1;
        int mid;
        while(l<=r)
        {
            mid=l+(r-l)/2;
            if(matrix[mid][m-1]==target)
                return true;
            else if(matrix[mid][m-1]>target)
                r=mid-1;
            else
                l=mid+1;
        }
        int row=l;
        if(row>=n)
            return false;
        l=0;
        r=m-1;
        while(l<=r)
        {
            mid=l+(r-l)/2;
            if(matrix[row][mid]==target)
                return true;
            else if(matrix[row][mid]>target)
                r=mid-1;
            else
                l=mid+1;
        }
        return false;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col=m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
        
 {% endhighlight %}
