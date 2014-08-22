---
layout: post
title: Spiral Matrix II
date: 2014-08-22 11:16:16
disqus: y
---

## 题意：
构造矩阵

## 要求：


## 思路：
模拟就好

## 更新：
总结leetcode数组题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int> > ans(n,vector<int>(n,0));
        int x=0;
        int y=0;
        int num=1;
        while(x<n)
        {
            for(int i=y;i<n;i++)
                ans[x][i]=num++;
            for(int i=x+1;i<n;i++)
                ans[i][n-1]=num++;
            if(x!=n-1)
                for(int i=n-2;i>=y;i--)
                    ans[n-1][i]=num++;
            if(y!=n-1)
                for(int i=n-2;i>x;i--)
                    ans[i][y]=num++;
            x++;
            y++;
            n--;
        }
        return ans;
    }
};

 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ans=[[[]for i in range(n)] for j in range(n)]
        start=0
        end=n-1
        num=1
        while start<end:
            for i in range(start,end):
                ans[start][i]=num
                num+=1
            for i in range(start,end):
                ans[i][end]=num
                num+=1
            for i in range(end,start,-1):
                ans[end][i]=num
                num+=1
            for i in range(end,start,-1):
                ans[i][start]=num
                num+=1
            start+=1
            end-=1
        if start==end:
            ans[start][start]=num
        return ans
 {% endhighlight %}
