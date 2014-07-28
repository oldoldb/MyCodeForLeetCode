---
layout: post
title: Search a 2D Matrix
date: 2014-07-28 15:52:16
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

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool findTarget(int row,int col,vector<vector<int> > &matrix,int target,int n,int m)
    {
        if(row>=n||col<0)
        {
            return false;
        }
        if(matrix[row][col]==target)
        {
            return true;
        }
        if(matrix[row][col]>target)
        {
            return findTarget(row,col-1,matrix,target,n,m);
        }
        else
        {
            return findTarget(row+1,col,matrix,target,n,m);
        }
    }
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int n=matrix.size();
        int m=matrix[0].size();
        return findTarget(0,m-1,matrix,target,n,m);
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
