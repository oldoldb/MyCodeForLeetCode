---
layout: post
title: Simplify Path
date: 2014-08-23 15:28:16
disqus: y
---

## 题意：
化简unix路径

## 要求：


## 思路：
用一个堆栈来模拟路径的行为，遇到"."不操作，遇到".."退栈，其他情况都压入堆栈。

## 更新：
总结leetcode堆栈题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string simplifyPath(string path) {
        stack<string>s;
        string str;
        int length=path.length();
        for(int i=0;i<=length;i++)
            if(path[i]=='/' || i==length)
            {
                if(str=="..")
                    if(!s.empty())
                        s.pop();
                else if(str!="." && str!="")
                    s.push(str);
                str="";
            }
            else
                str+=path[i];
        if(s.empty())
            return "/";
        string ans;
        while(!s.empty())
        {
            ans="/"+s.top()+ans;
            s.pop();
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        s=[]
        str=""
        length=len(path)
        for i in range(length+1):
            if i==length or path[i]=='/':
                if str=="..":
                    if len(s)!=0:
                        s.pop(-1)
                elif str!='.' and str!='':
                    s.append(str)
                str=""
            else:
                str+=path[i]
        if len(s)==0:
            return "/"
        ans=""
        while len(s)!=0:
            ans="/"+s[-1]+ans
            s.pop(-1)
        return ans
 {% endhighlight %}
