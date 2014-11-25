---
layout: post
title: Palindrome Number
date: 2014-08-23 10:36:16
disqus: y
---

## 题意：
判断一个数是不是回文数

## 要求：
- 负数不是回文数
- 不能将整数转换为字符串，因为题目要求不能增加额外空间
- 反转整数的时候注意越界问题

## 思路：
反转整数，判断反转后的整数时候和原数相同

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
            return false;
        int base=1;
        while(x/base>=10)
            base*=10;
        while(x)
        {
            int l=x/base;
            int r=x%10;
            if(l!=r)
                return false;
            x-=base*l;
            base/=100;
            x/=10;
        }
        return true;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        y=x
        ans=0
        while x:
            temp=x%10
            ans=ans*10+temp
            x/=10
        if ans==y:
            return True
        else:
            return False
 {% endhighlight %}
