---
layout: post
title: Rotate Image
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
将矩阵顺时针旋转90度

## 要求：


## 思路：
模拟

## 代码：

### C++:

{% highlight c++ %}
class Solution {
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int n=matrix.size();
        int start=0;
        int end=n-1;
        int width=n-1;
        int index=0;
        while(start<end)
        {
            for(int i=start;i<end;i++)
            {
                int temp=matrix[index][i];
                matrix[index][i]=matrix[width-i][index];
                matrix[width-i][index]=matrix[width-index][width-i];
                matrix[width-index][width-i]=matrix[i][width-index];
                matrix[i][width-index]=temp;
            }
            index++;
            start++;
            end--;
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
