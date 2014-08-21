---
layout: post
title: Maximal Rectangle
date: 2014-08-21 16:45:16
disqus: y
---

## 题意：
求矩阵中全1区域的最大面积

## 要求：


## 思路：
line[i][j]表示第i行第j列以上的最大的全一部分的长度，然后扫描每一行，像求最大直方图面积一样求最大矩形面积
http://www.cnblogs.com/easonliu/p/3657489.html

## 更新：
总结leetcode退栈题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxRectangleArea(vector<int> height)
    {
        stack<int> st;
        height.push_back(0);
        int n=height.size();
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(st.empty() || height[i]>height[st.top()])
                st.push(i);
            else
            {
                int index=st.top();
                st.pop();
                ans=max(ans,height[index]*(st.empty()?i:i-st.top()-1));
                i--;
            }
        }
        return ans;
    }
    int maximalRectangle(vector<vector<char> > &matrix) {
        int n=matrix.size();
        if(n==0)
            return 0;
        int m=matrix[0].size();
        vector<vector<int> > height(n,vector<int>(m,0));
        int ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
                if(i==0)
                    height[i][j]=(matrix[i][j]=='1'?1:0);
                else
                    height[i][j]=(matrix[i][j]=='1'?height[i-1][j]+1:0);
            ans=max(ans,maxRectangleArea(height[i]));
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
