---
layout: post
title: Edit Distance
date: 2014-08-19 16:07:16
disqus: y
---

## 题意：
求两个单词的编辑距离

## 要求：


## 思路：
dp[i][j]表示word1的前i个字母和word2的前j个字母的距离，则dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1](if word1[i]==word2[j])

## 更新:
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1=word1.length();
        int len2=word2.length();
        int **dp=new int*[len1+1];
        for(int i=0;i<=len1;i++)
            dp[i]=new int[len2+1];
        for(int i=0;i<=len1;i++)
            dp[i][0]=i;
        for(int i=0;i<=len2;i++)
            dp[0][i]=i;
        for(int i=1;i<=len1;i++)
        {
            for(int j=1;j<=len2;j++)
            {
                int ins=dp[i-1][j]+1;
                int del=dp[i][j-1]+1;
                int rep=dp[i-1][j-1]+(word1[i-1]==word2[j-1]?0:1);
                dp[i][j]=min(min(ins,del),rep);
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
    def minDistance(self, word1, word2):
        len1=len(word1)
        len2=len(word2)
        if len1==0 or len2==0:
            return max(len1,len2)
        dp=[[0 for i in range(len2+1)]for j in range(len1+1)]
        for i in range(len1+1):
            dp[i][0]=i
        for i in range(len2+1):
            dp[0][i]=i
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1]+1
                dp[i][j]=min(dp[i][j],dp[i-1][j]+1);
                dp[i][j]=min(dp[i][j],dp[i][j-1]+1);
        return dp[len1][len2]
 {% endhighlight %}
