---
layout: post
title: Scramble String
date: 2014-08-20 14:05:16
disqus: y
---

## 题意：
判断两个string是不是Scramble string

## 要求：


## 思路：
http://www.blogjava.net/sandy/archive/2013/05/22/399605.html
http://blog.csdn.net/pickless/article/details/11501443

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isScramble(string s1, string s2) {
        int n=s1.length();
        int m=s2.length();
        if(n!=m)
            return false;
        vector<vector<vector<bool> > > dp(n,vector<vector<bool> >(n,vector<bool>(false)));
        for(int len=0;len<n;len++)
            for(int i=0;i<n-len;i++)
                for(int j=0;j<n-len;j++)
                    if(len==0)
                        dp[i][j][len]=(s1[i]==s2[j]);
                    else
                        for(int k=0;k<len;k++)
                        {
                            dp[i][j][len]=(dp[i][j][k] && dp[i+k+1][j+k+1][len-k-1]) 
                            || (dp[i][j+len-k][k] && dp[i+k+1][j][len-k-1]);
                            if(dp[i][j][len])
                                break;
                        }
        return dp[0][0][n-1];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1)==0:
            return True
        lens1 = len(s1)
        ans = [[[0 for x in range(lens1)] for y in range(lens1)]for z in range(lens1)]
        for i in range(lens1):
            for j in range(len(s1)):
                ans[0][i][j] = (s1[i]==s2[j])
        for k in range(2,lens1+1):
            for i in range(lens1-k,-1,-1):
                for j in range(lens1-k,-1,-1):
                    flag = False;
                    for m in range(1,k):
                        if flag==True:
                            break
                        flag= ans[m-1][i][j] and ans[k-m-1][i+m][j+m] or ans[m-1][i][j+k-m] and ans[k-m-1][i+m][j]
                    ans[k-1][i][j]=flag
        return ans[lens1-1][0][0]
 {% endhighlight %}
