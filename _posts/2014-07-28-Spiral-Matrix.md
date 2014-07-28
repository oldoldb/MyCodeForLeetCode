---
layout: post
title: Spiral Matrix
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
按要求方向输出矩阵

## 要求：


## 思路：
模拟

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int> > &matrix) {
        vector<int>ans;
        int n=matrix.size();
        if(n==0)
        {
            return ans;
        }
        int m=matrix[0].size();
        if(m==0)
        {
            return ans;
        }
        int x=0;
        int y=0;
        while(x<n&&y<m)
        {
            for(int i=y;i<m;i++)
            {
                ans.push_back(matrix[x][i]);
            }
            for(int i=x+1;i<n;i++)
            {
                ans.push_back(matrix[i][m-1]);
            }
            if(x!=n-1)
            {
                for(int i=m-2;i>=y;i--)
                {
                    ans.push_back(matrix[n-1][i]);
                }
            }
            if(y!=m-1)
            {
                for(int i=n-2;i>x;i--)
                {
                    ans.push_back(matrix[i][y]);
                }
            }
            x++;
            y++;
            n--;
            m--;
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        ans=[]
        n=len(matrix)
        if n==0:
            return ans
        m=len(matrix[0])
        if m==0:
            return ans
        x=0
        y=0
        while x<n and y<m:
            for i in range(y,m):
                ans.append(matrix[x][i])
            for i in range(x+1,n):
                ans.append(matrix[i][m-1])
            if n-1!=x:
                for i in range(m-2,y-1,-1):
                    ans.append(matrix[n-1][i])
            if m-1!=y:
                for i in range(n-2,x,-1):
                    ans.append(matrix[i][y])
            x=x+1
            y=y+1
            n=n-1
            m=m-1
        return ans
 {% endhighlight %}
