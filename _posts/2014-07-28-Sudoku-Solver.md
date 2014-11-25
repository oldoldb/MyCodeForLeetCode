---
layout: post
title: Sudoku Solver
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
解数独

## 要求：


## 思路：
深搜

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool ok(vector<vector<char> >&board,int x,int y)
    {
        for(int i=0;i<9;i++)
        {
            if(i!=x&&board[i][y]==board[x][y])
            {
                return false;
            }
        }
        for(int j=0;j<9;j++)
        {
            if(j!=y&&board[x][j]==board[x][y])
            {
                return false;
            }
        }
        for(int i=x/3*3;i<x/3*3+3;i++)
        {
            for(int j=y/3*3;j<y/3*3+3;j++)
            {
                if(i!=x&&j!=y&&board[i][j]==board[x][y])
                {
                    return false;
                }
            }
        }
        return true;
    }
    bool dfs(vector<vector<char> >&board)
    {
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j]=='.')
                {
                    for(int k=1;k<=9;k++)
                    {
                        board[i][j]='0'+k;
                        if(ok(board,i,j)&&dfs(board))
                        {
                            return true;
                        }
                        board[i][j]='.';
                    }
                    return false;
                }
            }
        }
        return true;
    }
    void solveSudoku(vector<vector<char> > &board) {
        dfs(board);
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
