---
layout: post
title: Spiral Matrix II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
构造矩阵

## 要求：


## 思路：
模拟就好

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int> >ans;
        ans.resize(n);
        for(int i=0;i<n;i++)
        {
            ans[i].resize(n);
        }
        int start=0;
        int end=n-1;
        int num=1;
        while(start<end)
        {
            for(int i=start;i<end;i++)
            {
                ans[start][i]=num;
                num++;
            }
            for(int i=start;i<end;i++)
            {
                ans[i][end]=num;
                num++;
            }
            for(int i=end;i>start;i--)
            {
                ans[end][i]=num;
                num++;
            }
            for(int i=end;i>start;i--)
            {
                ans[i][start]=num;
                num++;
            }
            start++;
            end--;
        }
        if(start==end)
        {
            ans[start][start]=num;
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
