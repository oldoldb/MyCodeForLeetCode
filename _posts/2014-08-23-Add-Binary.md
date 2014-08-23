---
layout: post
title: Add Binary
date: 2014-08-23 13:17:16
disqus: y
---

## 题意：
模拟二进制加法

## 要求：


## 思路：
就和模拟大数加法一样

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string addBinary(string a, string b) {
        int n=a.length();
        int m=b.length();
        int flag=0;
        string ans="";
        int maxlen=max(m,n);
        for(int i=0;i<maxlen;i++)
        {
            int val1=i<n?a[n-1-i]-'0':0;
            int val2=i<m?b[m-1-i]-'0':0;
            int val=val1+val2+flag;
            flag=val/2;
            ans=char(val%2+'0')+ans;
        }
        return flag?"1"+ans:ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        len1=len(a)
        len2=len(b)
        p=len1-1
        q=len2-1
        sum=0
        add=0
        ans=""
        while p>=0 and q>=0:
            sum=int(a[p])-int('0')+int(b[q])-int('0')+add
            if sum>1:
                sum-=2
                add=1
            else:
                add=0
            ans+=str(sum+int('0'))
            p-=1
            q-=1
        while p>=0:
            sum=int(a[p])-int('0')+add
            if sum>1:
                sum-=2
                add=1
            else:
                add=0
            ans+=str(sum+int('0'))
            p-=1
        while q>=0:
            sum=int(b[q])-int('0')+add
            if sum>1:
                sum-=2
                add=1
            else:
                add=0
            ans+=str(sum+int('0'))
            q-=1
        if add:
            ans+='1'
        return ans[::-1]
 {% endhighlight %}
