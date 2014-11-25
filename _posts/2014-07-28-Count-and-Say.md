---
layout: post
title: Count and Say
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给定n，求满足要求的第n个序列

## 要求：


## 思路：
模拟

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string intToString(int n)
    {
        string ans="";
        while(n)
        {
            int temp=n%10;
            ans+=(temp+'0');
            n/=10;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
    string countAndSay(int n) {
        string str="1";
        string ans="1";
        for(int i=2;i<=n;i++)
        {
            str=ans;
            ans="";
            char last=str[0];
            int cnt=0;
            for(int j=0;j<=str.length();j++)
            {
                if(str[j]==last)
                {
                    cnt++;
                }
                else
                {
                    ans+=intToString(cnt);
                    ans+=last;
                    cnt=1;
                    last=str[j];
                }
            }
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @return a string
    def countAndSay(self, n):
        s="1"
        ans="1"
        for i in range(2,n+1):
            s=ans
            ans=""
            last=s[0]
            cnt=0
            for j in range(len(s)+1):
                if j==len(s) or s[j]!=last:
                    ans+=str(cnt)
                    ans+=last
                    cnt=1
                    if j!=len(s):
                        last=s[j]
                else:
                    cnt+=1
        return ans
 {% endhighlight %}
