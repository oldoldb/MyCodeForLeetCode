---
layout: post
title: String to Integer(atoi)
date: 2014-07-28 15:52:16
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

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int atoi(const char *str) {
        int num=0;
        bool flag=true;
        int len=strlen(str);
        int start=0;
        for(start=0;start<len;start++)
        {
            if(str[start]!=' ')
            {
                break;
            }
        }
        if(str[start]=='+')
        {
            start++;
        }
        if(str[start]=='-')
        {
            flag=false;
            start++;
        }
        for(int i=start;i<len;i++)
        {
            if(str[i]<'0'||str[i]>'9')
            {
                break;
            }
            if(num>INT_MAX/10 || num==INT_MAX/10 && (str[i]-'0')>INT_MAX%10)
            {
                if(flag)
                {
                    return INT_MAX;
                }
                else
                {
                    return INT_MIN;
                }
            }
            num=num*10+str[i]-'0';
        }
        if(flag)
        {
            return num;
        }
        else
        {
            return -num;
        }
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
