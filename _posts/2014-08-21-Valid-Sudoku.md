---
layout: post
title: Valid Sudoku
date: 2014-08-21 09:35:16
disqus: y
---

## 题意：
给定一个9*9数独，判断是不是合法的数独（不要求有解）

## 要求：


## 思路：
判断每一行每一列每一个3*3有没有重复的

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        int n=board.size();
        for(int i=0;i<n;i++)
        {
            vector<bool> row(n,false);
            for(int j=0;j<n;j++)
            {
                if(board[i][j]=='.')
                    continue;
                if(row[board[i][j]-'1'])
                    return false;
                row[board[i][j]-'1']=true;
            }
        }
        for(int j=0;j<n;j++)
        {
            vector<bool> col(n,false);
            for(int i=0;i<n;i++)
            {
                if(board[i][j]=='.')
                    continue;
                if(col[board[i][j]-'1'])
                    return false;
                col[board[i][j]-'1']=true;
            }
        }
        int t=sqrt(n);
        for(int i=0;i<n;i+=t)
        {
            for(int j=0;j<n;j+=t)
            {
                vector<bool> grid(n,false);
                for(int k=0;k<n;k++)
                {
                    int x=i+k/3;
                    int y=j+k%3;
                    if(board[x][y]=='.')
                        continue;
                    if(grid[board[x][y]-'1'])
                        return false;
                    grid[board[x][y]-'1']=true;
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
