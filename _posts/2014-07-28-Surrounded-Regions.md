---
layout: post
title: Surrounded Regions
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
矩阵由X和O组成，capture all the O surrounding by X

## 要求：


## 思路：
思路是从外围是’O'的开始深度往里走，这时候里面的‘O'就有两种命运，一种是跟外围的’O'是联通的，那么这些‘O'就可以存活，剩下的孤立的’O'就没办法了，就只能被‘X'了，为了区分这两种’O'，我们把联通 的‘O'改为另外一种统一而独立的字符，便于后期做恢复。这就是三步走（或两步）。

1）首先从外围的‘O'处深度搜索，见到链接的’O'就把他们都改为其他标识。

2）将剩余的孤立的’O'改为‘X'，同时，将遇到标识符改为’O'。

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int n;
    int m;
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
    bool ok(int x,int y)
    {
        return x>=0 && x<n && y>=0 && y<m;
    }
    void bfs(vector<vector<char> >&board,int x,int y)
    {
        queue<int>qx;
        queue<int>qy;
        qx.push(x);
        qy.push(y);
        board[x][y]='A';
        while(!qx.empty())
        {
            int xx=qx.front();
            qx.pop();
            int yy=qy.front();
            qy.pop();
            for(int i=0;i<4;i++)
            {
                int tx=xx+dx[i];
                int ty=yy+dy[i];
                if(ok(tx,ty) && board[tx][ty]=='O')
                {
                    qx.push(tx);
                    qy.push(ty);
                    board[tx][ty]='A';
                }
            }
        }
    }
    void solve(vector<vector<char>> &board) {
        n=board.size();
        if(n==0)
        {
            return;
        }
        m=board[0].size();
        if(m==0)
        {
            return;
        }
        for(int i=0;i<n;i++)
        {
            if(board[i][0]=='O')
            {
                bfs(board,i,0);
            }
            if(board[i][m-1]=='O')
            {
                bfs(board,i,m-1);
            }
        }
        for(int j=0;j<m;j++)
        {
            if(board[0][j]=='O')
            {
                bfs(board,0,j);
            }
            if(board[n-1][j]=='O')
            {
                bfs(board,n-1,j);
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(board[i][j]=='O')
                {
                    board[i][j]='X';
                }
                else if(board[i][j]=='A')
                {
                    board[i][j]='O';
                }
            }
        }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        n=len(board)
        if n==0:
            return
        m=len(board[0])
        if m==0:
            return
        for i in range(n):
            if board[i][0]=='O':
                self.bfs(board,i,0)
            if board[i][m-1]=='O':
                self.bfs(board,i,m-1)
        for j in range(m):
            if board[0][j]=='O':
                self.bfs(board,0,j)
            if board[n-1][j]=='O':
                self.bfs(board,n-1,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='A':
                    board[i][j]='O'
    def bfs(self,board,x,y):
        dx = []
        dx = [0,1,0,-1]
        dy = []
        dy = [1,0,-1,0]
        n=len(board)
        m=len(board[0])
        qx = collections.deque()
        qy = collections.deque()
        qx.append(x)
        qy.append(y)
        board[x][y]='A'
        while qx:
            xx=qx.popleft()
            yy=qy.popleft()
            for i in range(4):
                tx=xx+dx[i]
                ty=yy+dy[i]
                if self.ok(tx,ty,n,m) and board[tx][ty]=='O':
                    qx.append(tx)
                    qy.append(ty)
                    board[tx][ty]='A'
    def ok(self,x,y,n,m):
        return x>=0 and x<n and y>=0 and y<m
 {% endhighlight %}
