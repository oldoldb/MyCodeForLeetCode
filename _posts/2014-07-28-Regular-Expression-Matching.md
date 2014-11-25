---
layout: post
title: Regular Expression Matching
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
模拟正则匹配

## 要求：


## 思路：
递归：
http://blog.csdn.net/pickless/article/details/9043389
对于S[i]和P[j]：
如果P[j+1]!='*'，S[i] == P[j]=>匹配下一位(i+1, j+1)，S[i]!=P[j]=>匹配失败；
如果P[j+1]=='*'，S[i]==P[j]=>匹配下一位(i+1, j+2)或者(i, j+2)，S[i]!=P[j]=>匹配下一位(i,j+2)。
匹配成功的条件为S[i]=='\0' && P[j]=='\0'。

动态规划：
http://blog.sina.com.cn/s/blog_45b813200101bmyw.html
http://blog.csdn.net/linhuanmars/article/details/21145563

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        if(*p=='\0')
        {
            return *s=='\0';
        }
        if(*(p+1)!='*')
        {
            if(*s!='\0' && (*s==*p || *p=='.'))
            {
                return isMatch(s+1,p+1);
            }
        }
        else
        {
            while(*s!='\0' && (*s==*p || *p=='.'))
            {
                if(isMatch(s,p+2))
                {
                    return true;
                }
                s++;
            }
            return isMatch(s,p+2);
        }
        return false;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        lens = len(s)
        lenp = len(p)
        if lens==0 and lenp==0:
            return True
        if lenp==0:
            return False
        res=[[False for x in range(lenp+1)] for y in range(lens+1)]
        res[0][0]=True
        for i in range(lens+1):
            prechar='\0'
            preidex=0
            for j in range(1,lenp+1):
                if i>=1 and (p[j-1]=='.' or s[i-1]==p[j-1]):
                    res[i][j]=res[i-1][j-1]
                elif p[j-1]=='*':
                    if i>=1 and (prechar==s[i-1] or prechar=='.'):
                        res[i][j]=res[i-1][j] or res[i][j-1]
                    res[i][j]=res[i][j] or res[i][preidx]
                if p[j-1]!='*':
                    prechar=p[j-1]
                    preidx=j-1
        return res[lens][lenp]
 {% endhighlight %}
