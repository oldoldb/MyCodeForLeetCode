---
layout: post
title: Sudoku Solver
date: 2014-08-21 09:48:16
disqus: y
---

## 题意：
解数独

## 要求：


## 思路：
深搜

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool ok(vector<vector<char> > &board,int x,int y,int n)
    {
        for(int i=0;i<n;i++)
            if(x!=i && board[i][y]==board[x][y])
                return false;
        for(int j=0;j<n;j++)
            if(y!=j && board[x][j]==board[x][y])
                return false;
        int t=sqrt(n);
        int xx=x/t*t;
        int yy=y/t*t;
        for(int i=xx;i<xx+t;i++)
            for(int j=yy;j<yy+t;j++)
                if(x!=i && y!=j && board[i][j]==board[x][y])
                    return false;
        return true;
    }
    bool dfs(vector<vector<char> > &board,int pos,int n)
    {
        if(pos==n*n)
            return true;
        int x=pos/n;
        int y=pos%n;
        if(board[x][y]=='.')
            for(char c='1';c<='9';c++)
            {
                board[x][y]=c;
                if(ok(board,x,y,n) && dfs(board,pos+1,n))
                    return true;
                board[x][y]='.';
            }
        else if(dfs(board,pos+1,n))
            return true;
        return false;
    }
    void solveSudoku(vector<vector<char> > &board) {
        dfs(board,0,board.size());
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.dfs(board)
    def dfs(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for k in range(1,10):
                        board[i][j]=chr(ord('0')+k)
                        if self.ok(board,i,j) and self.dfs(board):
                            return True
                        board[i][j]='.'
                    return False
        return True
    def ok(self,board,x,y):
        for i in range(9):
            if i!=x and board[i][y]==board[x][y]:
                return False
        for j in range(9):
            if j!=y and board[x][j]==board[x][y]:
                return False
        for i in range(x/3*3,x/3*3+3):
            for j in range(y/3*3,y/3*3+3):
                if i!=x and j!=y and board[i][j]==board[x][y]:
                    return False
        return True
        
 {% endhighlight %}
