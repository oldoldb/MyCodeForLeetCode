---
layout: post
title: Valid Number 
date: 2014-08-24 16:43:16
disqus: y
---

## 题意：
判断字符串是否是有效的数字

## 要求：


## 思路：
。。各种情况，正负号，小数点，科学计数，前导0，后置0，

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isNumber(const char *s) {
        while(*s==' ')
            s++;
        if(*s=='\0')
            return false;
        if(*s=='-'||*s=='+')
            s++;
        bool flag=isdigit(*s);
        while(isdigit(*s))
            s++;
        if(*s=='.')
        {
            s++;
            flag=isdigit(*s)||flag;
            while(isdigit(*s))
                s++;
        }
        if(!flag)
            return false;
        if(*s=='e'||*s=='E')
        {
            s++;
            if(*s=='+'||*s=='-')
                s++;
            if(!isdigit(*s))
                return false;
            while(isdigit(*s))
                s++;
        }
        while(*s==' ')
            s++;
        return *s=='\0';
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

以后再补上
 {% endhighlight %}
