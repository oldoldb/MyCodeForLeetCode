---
layout: post
title: Integer to Roman
date: 2014-08-23 11:16:16
disqus: y
---

## 题意：
将一个整数转换成罗马数字，整数范围1-3999

## 要求：
无

## 思路：
开始在纠结各种400/900的表示什么的，后来想既然’M’,’D’什么的可以用来作为标记，那么“CM”,”CD”什么的为什么不能呢

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string intToRoman(int num) {
        string op[]={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int val[]={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        string ans="";
        for(int i=0;i<13;i++)
        {
            int cnt=num/val[i];
            while(cnt--)
                ans+=op[i];
            num%=val[i];
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a string
    def intToRoman(self, num):
        op=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans=""
        for i in range(13):
            cnt=num/val[i]
            while cnt:
                ans+=op[i]
                cnt=cnt-1
            num%=val[i]
        return ans;
 {% endhighlight %}
