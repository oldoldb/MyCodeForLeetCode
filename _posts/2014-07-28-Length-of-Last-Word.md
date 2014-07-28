---
layout: post
title: Length of Last Word
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求字符串中最后一个单词的长度

## 要求：

## 思路：
从后向前遍历字符串，记录第一个非空格的位置和之后的第一个空格的位置，作差就是最后一个单词的长度。注意各种特殊情况的判断

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int lengthOfLastWord(const char *s) {
        if(s==NULL)
        {
            return 0;
        }
        int len=strlen(s);
        int start=-1;
        for(int i=len-1;i>=0;i--)
        {
            if(s[i]!=' ')
            {
                start=i;
                break;
            }
        }
        if(start==-1)
        {
            return 0;
        }
        int end=-1;
        for(int i=start-1;i>=0;i--)
        {
            if(s[i]==' ')
            {
                end=i;
                break;
            }
        }
        return start-end;
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
