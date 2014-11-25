---
layout: post
title: Distinct Subsequences
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求S串中不同T串的个数

## 要求：


## 思路：
dp[i][j]表示S的前i个字符中包含T的前j个字符的个数，那么当S[i]==T[j]时，dp[i][j]=dp[i-1][j-1](前i-1个字符中匹配j-1个字符)+dp[i-1][j](前i-1个字符已经能和j个字符匹配);当S[i]!=T[j]时，就只能dp[i][j]=dp[i-1][j](前i-1个字符已经能和j个字符匹配）

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int numDistinct(string S, string T) {
        int len1=S.length();
        int len2=T.length();
        if(len1<len2)
        {
            return 0;
        }
        int **dp=new int*[len1+1];
        for(int i=0;i<=len1;i++)
        {
            dp[i]=new int[len2+1];
        }
        for(int i=0;i<=len1;i++)
        {
            dp[i][0]=1;
        }
        for(int i=1;i<=len2;i++)
        {
            dp[0][i]=0;
        }
        for(int j=1;j<=len2;j++)
        {
            for(int i=1;i<=len1;i++)
            {
                if(S[i-1]==T[j-1])
                {
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j];
                }
                else
                {
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        return dp[len1][len2];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        len1=len(S)
        len2=len(T)
        dp=[[0 for i in range(len2+1)] for j in range(len1+1)]
        for i in range(len1+1):
            dp[i][0]=1
        for i in range(1,len2+1):
            dp[0][i]=0
        for j in range(1,len2+1):
            for i in range(1,len1+1):
                if S[i-1]==T[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len1][len2]
 {% endhighlight %}
