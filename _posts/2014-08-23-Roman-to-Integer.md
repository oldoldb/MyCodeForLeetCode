---
layout: post
title: Roman to Integer
date: 2014-08-23 11:06:16
disqus: y
---

## 题意：
将一个罗马数字转换成整数，整数范围1-3999

## 要求：
无

## 思路：
这里我用map实现，建立罗马数字(char)与整数(int)的对应关系，遍历字符串，同时记录上一个字符，如果当前字符对应的整数大于上一个字符，那么就减去上一个字符对应的整数，否则加上

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int romanToInt(string s) {
        int ans=0;
        for(int i=s.length()-1;i>=0;i--)
        {
            if(s[i]=='I')
                ans+=(ans>=5?-1:1);
            else if(s[i]=='V')
                ans+=5;
            else if(s[i]=='X')
                ans+=(ans>=50?-10:10);
            else if(s[i]=='L')
                ans+=50;
            else if(s[i]=='C')
                ans+=(ans>=500?-100:100);
            else if(s[i]=='D')
                ans+=500;
            else if(s[i]=='M')
                ans+=1000;
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return an integer
    def romanToInt(self, s):
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        last=dic[s[0]]
        ans=0
        for i in range(1,len(s)):
            if dic[s[i]]>last:
                ans-=last
            else:
                ans+=last
            last=dic[s[i]]
        ans+=last
        return ans
 {% endhighlight %}
