---
layout: post
title: Count and Say
date: 2014-08-22 18:35:16
disqus: y
---

## 题意：
给定n，求满足要求的第n个序列

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
    string countAndSay(int n) {
        string ans="1";
        for(int i=1;i<n;i++)
        {
            stringstream ss;
            int cnt=0;
            char last=ans[0];
            for(int j=0;j<=ans.length();j++)
            {
                if(ans[j]==last)
                    cnt++;
                else
                {
                    ss<<cnt<<last;
                    cnt=1;
                    last=ans[j];
                }
            }
            ans=ss.str();
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
