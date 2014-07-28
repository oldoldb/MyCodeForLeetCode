---
layout: post
title: Evaluate Reverse Polish Notation
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
逆波兰表达式求值

## 要求：
注意负数

## 思路：
栈
另外Python的除法规则和C不太一样
对于-9/2
在python中为-5

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int cal(int x1,int x2,string op)
    {
        if(op=="+")
        {
            return x1+x2;
        }
        else if(op=="-")
        {
            return x1-x2;
        }
        else if(op=="*")
        {
            return x1*x2;
        }
        else
        {
            return x1/x2;
        }
    }
    int evalRPN(vector<string> &tokens) {
        stack<int>st;
        int num=0;
        for(vector<string>::iterator it=tokens.begin();it!=tokens.end();it++)
        {
            if(isdigit((*it)[0])||(*it).length()>1)
            {
                st.push(atoi((*it).c_str()));
            }
            else
            {
                int x2=st.top();
                st.pop();
                int x1=st.top();
                st.pop();
                st.push(cal(x1,x2,*it));
            }
        }
        return st.top();
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def cal(self,x1,x2,op):
        if op=="+":
            return x1+x2
        elif op=="-":
            return x1-x2
        elif op=="*":
            return x1*x2
        elif op=="/":
            if x1*x2<0:
                return -(abs(x1)/abs(x2))
            else:
                return abs(x1)/abs(x2)
        else:
            return 100
    def evalRPN(self, tokens):
        st=[] 
        for i in range(len(tokens)):
            if tokens[i].isdigit() or len(tokens[i])>1:
                st.append(int(tokens[i]))
            else:
                x2=st.pop()
                x1=st.pop()
                st.append(self.cal(x1,x2,tokens[i]))
        return st[0]
 {% endhighlight %}
