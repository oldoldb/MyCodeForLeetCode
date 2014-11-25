---
layout: post
title: Valid Parentheses
date: 2014-08-21 18:27:16
disqus: y
---

## 题意：
判断括号匹配是否正确

## 要求：

## 思路：
栈

## 更新：
总结leetcode堆栈题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='(' || s[i]=='{' || s[i]=='[')
                st.push(s[i]);
            else if(st.empty())
                return false;
            else
            {
                char ch=st.top();
                st.pop();
                if(ch=='('&&s[i]==')' || ch=='['&&s[i]==']' || ch=='{'&&s[i]=='}')
                    continue;
                else
                    return false;
            }
        }
        return st.empty();
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a boolean
    def isValid(self, s):
        st=[0 for i in range(1000)]
        top=0
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                st[top]=s[i]
                top+=1
            else:
                if top==0:
                    return False
                top-=1
                temp=st[top]
                if s[i]==')' and temp=='(' or s[i]==']' and temp=='[' or s[i]=='}' and temp=='{':
                    continue
                else:
                    return False
        if top!=0:
            return False
        else:
            return True
 {% endhighlight %}
