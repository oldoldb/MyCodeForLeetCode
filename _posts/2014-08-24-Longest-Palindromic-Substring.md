---
layout: post
title: Longest Palindromic Substring
date: 2014-08-24 16:30:16
disqus: y
---

## 题意：
求最长回文子串

## 要求：


## 思路：
O(n^2)的算法有动态规划（需要额外空间）和中心扩展法
O(n)的算法是马拉车算法，还不会。

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int longestPalindromeHelper(string s,int i,int j)
    {
        int n=s.length();
        while(i>=0&&j<n&&s[i]==s[j])
        {
            i--;
            j++;
        }
        return j-i-1;
    }
    string longestPalindrome(string s) {
        int n=s.length();
        int maxlen=1;
        int startpos=0;
        for(int i=0;i<n;i++)
        {
            int len1=longestPalindromeHelper(s,i,i);
            int len2=0;
            if(i+1<n)
                len2=longestPalindromeHelper(s,i,i+1);
            int curlen=max(len1,len2);
            if(curlen>maxlen)
            {
                maxlen=curlen;
                if(maxlen%2)
                    startpos=i-maxlen/2;
                else
                    startpos=i-(maxlen-1)/2;
            }
        }
        return s.substr(startpos,maxlen);
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

以后再补上
 {% endhighlight %}
