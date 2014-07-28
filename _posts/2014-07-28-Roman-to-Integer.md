---
layout: post
title: Roman to Integer
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
将一个罗马数字转换成整数，整数范围1-3999

## 要求：
无

## 思路：
这里我用map实现，建立罗马数字(char)与整数(int)的对应关系，遍历字符串，同时记录上一个字符，如果当前字符对应的整数大于上一个字符，那么就减去上一个字符对应的整数，否则加上

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int romanToInt(string s) {
        map<char,int>mp;
        mp['I']=1;
        mp['V']=5;
        mp['X']=10;
        mp['L']=50;
        mp['C']=100;
        mp['D']=500;
        mp['M']=1000;
        int len=s.length();
        int ans=0;
        int last=mp[s[0]];
        for(int i=1;i<len;i++)
        {
            if(mp[s[i]]>last)
            {
                ans-=last;
            }
            else
            {
                ans+=last;
            }
            last=mp[s[i]];
        }
        ans+=last;
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
