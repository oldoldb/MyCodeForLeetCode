---
layout: post
title: Word Break
date: 2014-08-20 11:00:16
disqus: y
---

## 题意：
给定一个string和一个单词集合，判断string是否可以恰巧被分割成单词

## 要求：


## 思路：
dp[i]  表示源串的前i个字符可以满足分割，那么 dp[ j ] 满足分割的条件是存在k 使得 dp [k] && substr[k,j]在字典里。

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        int len=s.length();
        vector<bool>dp(len,false);
        dp[0]=true;
        for(int i=0;i<len;i++)
            if(dp[i])
                for(int j=1;j<=len;j++)
                    if(dict.count(s.substr(i,j))>0)
                        dp[i+j]=true;
        return dp[len];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n=s.__len__()
        dp = [False for x in range(n+1)]
        dp[0]=True
        for i in range(n):
            if dp[i]==True:
                for len in range(1,n+1-i):
                    if s[i:i+len] in dict:
                        dp[i+len]=True
        return dp[n]
        
 {% endhighlight %}
