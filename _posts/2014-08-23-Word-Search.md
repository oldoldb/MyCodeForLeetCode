---
layout: post
title: Word Search
date: 2014-08-23 15:03:16
disqus: y
---

## 题意：
判断一个矩阵中是否有给定单词

## 要求：


## 思路：
典型的深搜

## 更新：
总结leetcode搜索题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
    bool ok(int x,int y,int n,int m)
    {
        return x>=0 && x<n && y>=0 && y<m;
    }
    bool dfs(vector<vector<char> >&board,int n,int m,int len,string word,vector<vector<bool> >&visit,int x,int y,int pos)
    {
        if(pos==len)
            return true;
        for(int i=0;i<4;i++)
        {
            int tx=x+dx[i];
            int ty=y+dy[i];
            if(ok(tx,ty,n,m) && visit[tx][ty]==false && board[tx][ty]==word[pos])
            {
                visit[tx][ty]=true;
                if(dfs(board,n,m,len,word,visit,tx,ty,pos+1))
                    return true;
                visit[tx][ty]=false;
            }
        }
        return false;
    }
    bool exist(vector<vector<char> > &board, string word) {
        int len=word.length();
        if(len==0)
            return true;
        int n=board.size();
        if(n==0)
            return false;
        int m=board[0].size();
        vector<vector<bool> >visit(n, vector<bool>(m,false));
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(board[i][j]==word[0])
                {
                    visit[i][j]=true;
                    if(dfs(board,n,m,len,word,visit,i,j,1))
                        return true;
                    visit[i][j]=false;
                }
        return false;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        length=len(word)
        if length==0:
            return True
        n=len(board)
        if n==0:
            return False
        m=len(board[0])
        if m==0:
            return False
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        visit=[[False for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    visit[i][j]=True
                    if self.dfs(board,n,m,length,visit,word,i,j,1,dx,dy)==True:
                        return True
                    visit[i][j]=False
        return False
    def dfs(self,board,n,m,length,visit,word,x,y,pos,dx,dy):
        if pos==length:
            return True
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if self.ok(tx,ty,n,m)==True and visit[tx][ty]==False and board[tx][ty]==word[pos]:
                visit[tx][ty]=True
                if self.dfs(board,n,m,length,visit,word,tx,ty,pos+1,dx,dy)==True:
                    return True
                visit[tx][ty]=False
        return False
    def ok(self,x,y,n,m):
        return x>=0 and x<n and y>=0 and y<m
 {% endhighlight %}
