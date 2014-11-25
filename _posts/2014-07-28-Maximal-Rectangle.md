---
layout: post
title: Maximal Rectangle
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求矩阵中全1区域的最大面积

## 要求：


## 思路：
line[i][j]表示第i行第j列以上的最大的全一部分的长度，然后扫描每一行，像求最大直方图面积一样求最大矩形面积
http://www.cnblogs.com/easonliu/p/3657489.html

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxarea(vector<int> &line)
    {
        if(line.size()==0)
        {
            return 0;
        }
        stack<int>s;
        line.push_back(0);
        int sum=0;
        for(int i=0;i<line.size();i++)
        {
            if(s.empty() || line[i]>line[s.top()])
            {
                s.push(i);
            }
            else
            {
                int temp=s.top();
                s.pop();
                sum=max(sum,line[temp]*(s.empty()?i:i-s.top()-1));
                i--;
            }
        }
        return sum;
    }
    int maximalRectangle(vector<vector<char> > &matrix) {
        int n=matrix.size();
        if(n==0)
        {
            return 0;
        }
        int m=matrix[0].size();
        if(m==0)
        {
            return 0;
        }
        vector<vector<int> >lines(n,vector<int>(m,0));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(i==0)
                {
                    lines[i][j]=matrix[i][j]=='1'?1:0;
                }
                else
                {
                    lines[i][j]+=matrix[i][j]=='1'?lines[i-1][j]+1:0;
                }
            }
        }
        int ans=0;
        for(int i=0;i<n;i++)
        {
            ans=max(ans,maxarea(lines[i]));
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        n=len(matrix)
        if n==0:
            return 0
        m=len(matrix[0])
        if m==0:
            return 0
        lines=[[0 for x in range(m)]for y in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0:
                    lines[i][j]=1 if matrix[i][j]=='1' else 0
                else:
                    lines[i][j]+=lines[i-1][j]+1 if matrix[i][j]=='1' else 0
        ans = 0
        for i in range(n):
            ans=max(ans,self.maxarea(lines[i]));
        return ans
    def maxarea(self,line):
        if len(line)==0:
            return 0
        s=[]
        line.append(0)
        sum=0
        i=0
        while i<len(line):
            if len(s)==0 or line[i]>line[s[-1]]:
                s.append(i)
            else:
                temp=s[-1]
                s.pop(-1)
                sum=max(sum,line[temp]*(i if len(s)==0 else i-s[-1]-1))
                i=i-1
            i=i+1
        return sum
        
 {% endhighlight %}
