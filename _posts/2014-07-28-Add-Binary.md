---
layout: post
title: Add Binary
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
模拟二进制加法

## 要求：


## 思路：
就和模拟大数加法一样

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string addBinary(string a, string b) {
        int len1=a.length();
        int len2=b.length();
        int p=len1-1;
        int q=len2-1;
        string ans="";
        int sum=0;
        int add=0;
        while(p>=0&&q>=0)
        {
            sum=(a[p]-'0')+(b[q]-'0')+add;
            if(sum>1)
            {
                sum-=2;
                add=1;
            }
            else
            {
                add=0;
            }
            ans+=(sum+'0');
            p--;
            q--;
        }
        while(p>=0)
        {
            sum=(a[p]-'0')+add;
            if(sum>1)
            {
                sum=0;
                add=1;
            }
            else
            {
                add=0;
            }
            ans+=(sum+'0');
            p--;
        }
        while(q>=0)
        {
            sum=(b[q]-'0')+add;
            if(sum>1)
            {
                sum=0;
                add=1;
            }
            else
            {
                add=0;
            }
            ans+=(sum+'0');
            q--;
        }
        if(add)
        {
            ans+='1';
        }
        reverse(ans.begin(),ans.end());
        return ans;
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
