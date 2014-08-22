---
layout: post
title: Multiply Strings
date: 2014-08-22 19:07:16
disqus: y
---

## 题意：
大数乘法

## 要求：


## 思路：
模拟

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1=="0" || num2=="0")
            return "0";
        int len1=num1.length();
        int len2=num2.length();
        int len=len1+len2;
        int *n1=new int[len1];
        int *n2=new int[len2];
        int *ans=new int[len];
        memset(ans,0,sizeof(int)*len);
        for(int i=0;i<len1;i++)
            n1[i]=num1[i]-'0';
        for(int i=0;i<len2;i++)
            n2[i]=num2[i]-'0';
        for(int i=0;i<len1;i++)
            for(int j=0;j<len2;j++)
                ans[i+j+1]+=n1[i]*n2[j];
        string res="";
        for(int i=len-1;i>=0;i--)
        {
            if(i>0)
                ans[i-1]+=ans[i]/10;
            ans[i]%=10;
            res=char(ans[i]+'0')+res;        
        }
        res=(res[0]=='0'?res.substr(1):res);
        return res;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1=="0" or num2=="0":
            return "0"
        len1=len(num1)
        len2=len(num2)
        len3=len1+len2
        n1=[ord(num1[x])-ord('0') for x in range(len1)]
        n2=[ord(num2[x])-ord('0') for x in range(len2)]
        res=[0 for x in range(len3)]
        for i in range(len1):
            for j in range(len2):
                res[i+j+1]+=n1[i]*n2[j]
        ss=""
        for i in range(len3-1,-1,-1):
            if i>0:
                res[i-1]+=res[i]/10
            res[i]%=10
            ss=chr(res[i]+ord('0'))+ss
        ss=ss[1:] if ss[0]=='0' else ss
        return ss
 {% endhighlight %}
