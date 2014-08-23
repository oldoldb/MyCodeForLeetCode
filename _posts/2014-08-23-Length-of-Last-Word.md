---
layout: post
title: Length of Last Word
date: 2014-08-23 14:32:16
disqus: y
---

## 题意：
求字符串中最后一个单词的长度

## 要求：

## 思路：
从后向前遍历字符串，记录第一个非空格的位置和之后的第一个空格的位置，作差就是最后一个单词的长度。注意各种特殊情况的判断

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int lengthOfLastWord(const char *s) {
        int cnt=0;
        int ans=0;
        while(*s)
        {
            cnt=*s==' '?0:cnt+1;
            ans=cnt>0?cnt:ans;
            s++;
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s)==0:
            return 0
        start=-1
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                start=i;
                break;
        if start==-1:
            return 0
        end=-1
        for i in range(start-1,-1,-1):
            if s[i]==' ':
                end=i
                break
        return start-end
 {% endhighlight %}
