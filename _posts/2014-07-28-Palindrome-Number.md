---
layout: post
title: Palindrome Number
date: 2014-07-28 15:52:16
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

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
        int base=10;
        int y=x;
        int ans=0;
        while(x)
        {
            int temp=x%base;
            ans=ans*10+temp;
            x/=base;
        }
        if(y==ans)
        {
            return true;
        }
        else
        {
            return false;
        }
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
