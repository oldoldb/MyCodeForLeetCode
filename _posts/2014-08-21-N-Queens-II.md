---
layout: post
title: N-Queens II
date: 2014-08-21 10:15:16
disqus: y
---

## 题意：
经典八皇后

## 要求：
无

## 思路：
深搜，dfs(int pos)代表搜每一行，放置时遍历每一列，如果符合条件（同列未放，对角线未放）就放

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool ok(vector<int> visit,int endRow)
    {
        for(int row=0;row<endRow;row++)
            if(visit[row]==visit[endRow] || abs(visit[row]-visit[endRow]) == endRow-row)
                return false;
        return true;
    }
    void dfs(vector<int> &visit,int n,int row,int &ans)
    {
        if(row==n)
        {
            ans++;
            return;
        }
        for(int col=0;col<n;col++)
        {
            visit[row]=col;
            if(ok(visit,row))  
                dfs(visit,n,row+1,ans);
        }
    }
    int totalNQueens(int n) {
        vector<int> visit(n,0);
        int ans=0;
        dfs(visit,n,0,ans);
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
