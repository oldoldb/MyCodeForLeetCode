---
layout: post
title: Set Matrix Zeroes
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给定一个矩阵，如果某元素为0，那么将整行整列都置为0

## 要求：
空间复杂度O(1)

## 思路：
常数空间的话，第一可以考虑是不是固定数量的几个变量能搞定；否则可以考虑是不是问题本身已经提供了足够的空间。
这道题属于后者，就是利用矩阵的第一行和第一列来作为辅助空间使用。不用开辟新的存储空间。方法就是：
1.先确定第一行和第一列是否需要清零
即，看看第一行中是否有0，记下来。也同时记下来第一列中有没有0。

2.扫描剩下的矩阵元素，如果遇到了0，就将对应的第一行和第一列上的元素赋值为0
这里不用担心会将本来第一行或第一列的1改成了0，因为这些值最后注定要成为0的，比如matrix[i][j]==0，那么matrix[i][0]处在第i行，matrix[0][j]处于第j列，最后都要设置为0的。

3.根据第一行和第一列的信息，已经可以将剩下的矩阵元素赋值为结果所需的值了即，拿第一行为例，如果扫描到一个0，就将这一列都清0.

4.根据1中确定的状态，处理第一行和第一列。
如果最开始得到的第一行中有0的话，就整行清零。同理对列进行处理。

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        int row = matrix.size();
        if(row==0)
        {
            return ;
        }
        int col = matrix[0].size();
        if(col==0)
        {
            return ;
        }
        bool isFirstRowZero = false;
        bool isFirstColZero = false;
        for(int i=0;i<row;i++)
        {
            if(matrix[i][0]==0)
            {
                isFirstColZero = true;
                break;
            }
        }
        for(int j=0;j<col;j++)
        {
            if(matrix[0][j]==0)
            {
                isFirstRowZero = true;
                break;
            }
        }
        for(int i=1;i<row;i++)
        {
            for(int j=1;j<col;j++)
            {
                if(matrix[i][j]==0)
                {
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }
        for(int i=1;i<row;i++)
        {
            for(int j=1;j<col;j++)
            {
                if(matrix[i][0]==0 || matrix[0][j]==0)
                {
                    matrix[i][j]=0;
                }
            }
        }
        if(isFirstRowZero)
        {
            for(int j=0;j<col;j++)
            {
                matrix[0][j]=0;
            }
        }
        if(isFirstColZero)
        {
            for(int i=0;i<row;i++)
            {
                matrix[i][0]=0;
            }
        }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row = len(matrix)
        if row==0:
            return 
        col = len(matrix[0])
        if col==0:
            return
        isFirstRowZero = False
        isFirstColZero = False
        for i in range(row):
            if matrix[i][0]==0:
                isFirstColZero=True
                break
        for j in range(col):
            if matrix[0][j]==0:
                isFirstRowZero=True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if isFirstRowZero:
            for j in range(col):
                matrix[0][j]=0
        if isFirstColZero:
            for i in range(row):
                matrix[i][0]=0
 {% endhighlight %}
