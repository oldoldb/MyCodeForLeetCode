---
layout: post
title: Valid Sudoku
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给定一个9*9数独，判断是不是合法的数独（不要求有解）

## 要求：


## 思路：
判断每一行每一列每一个3*3有没有重复的

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        int row[9];
        int col[9];
        for(int i=0;i<9;i++)
        {
            memset(row,0,sizeof(row));
            memset(col,0,sizeof(col));
            for(int j=0;j<9;j++)
            {
                if(board[i][j]!='.')
                {
                    if(row[board[i][j]-'1'])
                    {
                        return false;
                    }
                    else
                    {
                        row[board[i][j]-'1']=1;
                    }
                }
                if(board[j][i]!='.')
                {
                    if(col[board[j][i]-'1'])
                    {
                        return false;
                    }
                    else
                    {
                        col[board[j][i]-'1']=1;
                    }
                }
            }
        }
        int grid[9];
        for(int i=0;i<9;i+=3)
        {
            for(int j=0;j<9;j+=3)
            {
                memset(grid,0,sizeof(grid));
                for(int k=0;k<9;k++)
                {
                    if(board[i+k/3][j+k%3]!='.')
                    {
                        if(grid[board[i+k/3][j+k%3]-'1'])
                        {
                            return false;
                        }
                        else
                        {
                            grid[board[i+k/3][j+k%3]-'1']=1;
                        }
                    }
                }
            }
        }
        return true;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        row = [0 for i in range(9)]
        col = [0 for i in range(9)]
        for i in range(9):
            row = [0 for x in range(9)]
            col = [0 for x in range(9)]
            for j in range(9):
                if board[i][j]!='.':
                    if row[int(board[i][j])-1] == 1:
                        return False
                    else:
                        row[int(board[i][j])-1]=1
                if board[j][i]!='.':
                    if col[int(board[j][i])-1] == 1:
                        return False
                    else:
                        col[int(board[j][i])-1]=1
        grid = [0 for i in range(9)]
        for i in range(0,9,3):
            for j in range(0,9,3):
                grid = [0 for x in range(9)]
                for k in range (9):
                    if board[i+k/3][j+k%3]!='.':
                        if grid[int(board[i+k/3][j+k%3])-1] == 1:
                            return False
                        else:
                            grid[int(board[i+k/3][j+k%3])-1]=1
        return True
 {% endhighlight %}
