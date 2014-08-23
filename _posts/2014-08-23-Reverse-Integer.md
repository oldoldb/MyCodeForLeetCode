---
layout: post
title: Reverse Integer
date: 2014-08-23 10:15:16
disqus: y
---

## 题意：
反转整数

## 要求：
注意负数情况，注意原数末尾位0的情况

## 思路：
考虑到上述两点就比较简单了，利用除法和取余一位一位的取好了
但题目中还有这样一些信息，如果反转后的整数溢出了怎么办？我想这里如果超过了最大范围那么应该是需要提前定义一个标记变量，在原来的数字有溢出危险时就报错；或者用字符串来处理；

## 更新：
总结leetcode数学题目

## 代码：
### C++:

{% highlight c++ %}
class Solution {
public:
    int reverse(int x) {
        long long ans=0;
        while(x)
        {
            ans=ans*10+x%10;
            if(ans>INT_MAX)
                return INT_MAX;
            if(ans<INT_MIN) 
                return INT_MIN;
            x/=10;
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @return an integer
    def reverse(self, x):
        flag=False
        if x==0:
            return x
        elif x<0:
            flag=True
            x=-x
        ans=0
        while x:
            ans=ans*10+x%10
            x/=10
        if flag:
            return -ans
        else:
            return ans        
 {% endhighlight %}
