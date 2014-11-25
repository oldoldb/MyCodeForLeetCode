---
layout: post
title: String to Integer(atoi)
date: 2014-08-22 19:35:16
disqus: y
---

## 题意：
实现库函数atoi()

## 要求：
- 不规则输入,但是有效,”-3924x8fc”,” + 413”
- 无效格式,” ++c”, ” ++1”
- 溢出数据,”2147483648”


## 思路：
注意特殊情况的判断
参考了《手写代码必备手册》

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int atoi(const char *str) {
        int start=0;
        while(str[start]==' ')
            start++;
        bool flag=true;
        if(str[start]=='+')
            start++;
        else if(str[start]=='-')
        {
            flag=false;
            start++;
        }
        int ans=0;
        for(int i=start;i<strlen(str);i++)
        {
            if(!isdigit(str[i]))
                break;
            if(ans>INT_MAX/10 || ans==INT_MAX/10 && str[i]-'0'>INT_MAX%10)
                if(flag)
                    return INT_MAX;
                else
                    return INT_MIN;
            ans=ans*10+str[i]-'0';
        }
        return flag?ans:-ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return an integer
    def atoi(self, str):
        if str=="":
            return 0
        num=0
        flag=True
        n=len(str)
        start=0
        while str[start]==' ':
            start+=1
        if str[start]=='+':
            start+=1
        if str[start]=='-':
            start+=1
            flag=False
        for i in range(start,n):
            if str[i]<'0' or str[i]>'9':
                break
            if num>2147483647/10 or num==2147483647/10 and int(str[i])-int('0')>2147483647%10:
                if flag:
                    return 2147483647
                else:
                    return -2147483648
            num=num*10+int(str[i])-int('0')
        if flag:
            return num
        else:
            return -num
 {% endhighlight %}
