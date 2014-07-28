---
layout: post
title: N-Queens II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
经典八皇后

## 要求：
无

## 思路：
深搜，dfs(int pos)代表搜每一行，放置时遍历每一列，如果符合条件（同列未放，对角线未放）就放

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int queen[15];
    int ans=0;
    bool isok(int pos)
    {
        for(int i=0;i<pos;i++)
        {
            if(queen[i]==queen[pos])
            {
                return false;
            }
            if(abs(i-pos)==abs(queen[i]-queen[pos]))
            {
                return false;
            }
        }
        return true;
    }
    void dfs(int pos,int n)
    {
        if(pos==n)
        {
            ans++;
            return;
        }
        for(int i=0;i<n;i++)
        {
            queen[pos]=i;
            if(isok(pos))
            {
                dfs(pos+1,n);
            }
        }
    }
    int totalNQueens(int n) {
        dfs(0,n);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    def isok(self,pos,queen):
        for i in range(pos):
            if queen[i]==queen[pos]:
                return False
            if abs(i-pos)==abs(queen[i]-queen[pos]):
                return False
        return True
    def dfs(self,pos,n,queen,ans):
        if pos==n:
            ans[0]=ans[0]+1
            return 
        for i in range(n):
            queen[pos]=i
            if self.isok(pos,queen):
                self.dfs(pos+1,n,queen,ans)
    
    # @return an integer
    def totalNQueens(self, n):
        queen=[0 for i in range(15)]
        ans=[0]
        self.dfs(0,n,queen,ans)
        return ans[0]
 {% endhighlight %}
