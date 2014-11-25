---
layout: post
title: ZigZag Conversion
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给定字符串text和行数nRows,求zigzag转换后的string

## 要求：


## 思路：
向下扫，对角线扫，简单的模拟

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string convert(string s, int nRows) {
        if(nRows==1)
        {
            return s;
        }
        string ans[nRows];
        for(int i=0;i<s.length(); )
        {
            for(int j=0;j<nRows&&i<s.length();j++)
            {
                ans[j]+=s[i];
                i++;
            }
            for(int j=nRows-2;j>0&&i<s.length();j--)
            {
                ans[j]+=s[i];
                i++;
            }
        }
        string str="";
        for(int i=0;i<nRows;i++)
        {
            str+=ans[i];
        }
        return str;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        ans = ["" for x in range(nRows)]
        i = 0
        while i < len(s):
            j = 0
            while j < nRows and i < len(s):
                ans[j] += s[i]
                i = i + 1
                j = j + 1
            j = nRows - 2 
            while j > 0 and i < len(s):
                ans[j] += s[i]
                i = i + 1
                j = j - 1
        ansstr = ""
        for i in range(nRows):
            ansstr+=ans[i]
        return ansstr
 {% endhighlight %}
