---
layout: post
title: Rotate Image
date: 2014-08-22 17:20:16
disqus: y
---

## 题意：
将矩阵顺时针旋转90度

## 要求：


## 思路：
模拟

##　更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int n=matrix.size()-1;
        for(int i=0;i<n;i++)
            for(int j=i;j<n-i;j++)
            {
                int x=i;
                int y=j;
                int prev=matrix[x][y];
                int next;
                for(int k=0;k<4;k++)
                {
                    next=matrix[y][n-x];
                    matrix[y][n-x]=prev;
                    prev=next;
                    int temp=x;
                    x=y;
                    y=n-temp;
                }
            }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n=len(matrix)
        start=0
        end=n-1
        width=n-1
        index=0
        while start<end:
            for i in range(start,end):
                matrix[index][i],matrix[width-i][index],matrix[width-index][width-i],matrix[i][width        -index]=matrix[width-i][index],matrix[width-index][width-i],matrix[i][width-index],matrix[index][i]
            index+=1
            start+=1
            end-=1
        return matrix
 {% endhighlight %}
