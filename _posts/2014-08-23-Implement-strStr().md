---
layout: post
title: Implement strStr()
date: 2014-08-23 16:17:16
disqus: y
---

## 题意：
实现库函数strstr()

## 要求：
无

## 思路：
只会暴力的方法
平时指针用的少，写出的代码不那么好看
注意及时跳出循环，否则会T

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    char *strStr(char *haystack, char *needle) {
        if(!*needle)
            return haystack;
        char *p1;
        char *p2;
        int len2=0;
        for(p2=needle;*p2;p2++)
            len2++;
        for(p1=haystack;*(p1+len2-1);p1++)
        {
            bool flag=true;
            for(p2=needle;*p2;p2++)
                if(*p2!=*(p2-needle+p1))
                {
                    flag=false;
                    break;
                }
            if(flag)
                return p1;
        }
        return NULL;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(needle)==0:
            return haystack
        for i in range(len(haystack)-len(needle)+1):
            flag=True
            for j in range(len(needle)):
                if needle[j]!=haystack[i+j]:
                    flag=False
                    break
            if flag:
                return haystack[i:]
        return None
 {% endhighlight %}
