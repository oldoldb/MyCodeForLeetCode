---
layout: post
title: Interleaving String
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
判断s3是否是由s1和s2交叉组成

## 要求：


## 思路：
很简单的动态规划,dp[i][j]表示s1的前i位和s2的前j位是否与s3的前i+j位匹配

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n=s1.length();
        int m=s2.length();
        int len=s3.length();
        if(n+m!=len)
        {
            return false;
        }
        vector<vector<bool> >dp(n+1, vector<bool>(m+1,false));
        dp[0][0]=true;
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=m;j++)
            {
                int pos=i+j;
                if(i>=1 && s1[i-1]==s3[pos-1])
                {
                    dp[i][j]=dp[i][j]||dp[i-1][j];
                }
                if(j>=1 && s2[j-1]==s3[pos-1])
                {
                    dp[i][j]=dp[i][j]||dp[i][j-1];
                }
            }
        }
        return dp[n][m];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if len1+len2!=len3:
            return False
        dp=[[False for x in range(len2+1)] for y in range(len1+1)]
        dp[0][0]=True
        for i in range(len1+1):
            for j in range(len2+1):
                pos=i+j
                if i>=1 and s1[i-1]==s3[pos-1]:
                    dp[i][j]=dp[i][j] or dp[i-1][j]
                if j>=1 and s2[j-1]==s3[pos-1]:
                    dp[i][j]=dp[i][j] or dp[i][j-1]
        return dp[len1][len2]
 {% endhighlight %}
