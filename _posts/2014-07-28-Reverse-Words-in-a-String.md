---
layout: post
title: Reverse Words in a String
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
翻转字符串中的单词，例如s=“the sky is blue”,return “blue is sky the”

## 要求：
注意空串
注意前导和后续的’ ‘
注意非字符符号

## 思路：
首先去掉前导和后续’ ‘,然后将单词入栈

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void reverseWords(string &s) {
        if(s=="")
        {
            return ;
        }
        int n=s.length();
        stack<string>st;
        int begin=0;
        int end=n-1;
        while(s[begin]==' ')
        {
            begin++;
        }
        if(begin>end)
        {
            s="";
            return ;
        }
        while(s[end]==' ')
        {
            end--;
        }
        end++;
        string word="";
        for(int i=begin;i<end;i++)
        {
            if(s[i]==' ')
            {
                if(word=="")
                {
                    continue;
                }
                st.push(word);
                word="";
                continue;
            }
            word+=s[i];
        }
        st.push(word);
        string ans="";
        while(st.size()>0)
        {
            string temp=st.top();
            st.pop();
            ans+=temp;
            if(st.size())
            {
                ans+=" ";
            }
        }
        s=ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @return a string
    def reverse(self,begin,end,s):
        while s[begin].isalpha():
            begin+=1
        while s[end].isalpha():
            end-=1
        while begin<end:
            s[begin],s[end]=s[end],s[begin]
            begin+=1
            end-=1
    def reverseWords(self, s):
        if s.strip()=='':
            return ''
        n=len(s)
        top=0
        st=[]
        begin=0
        end=n-1
        while s[begin]==' ':
            begin+=1
        while s[end]==' ':
            end-=1
        if begin>end:
            return ' '
        while s[end]==' ':
            end-=1
        end+=1
        word=""
        for i in range(begin,end):
            if s[i]==' ':
                if word=="":
                    continue
                st.append(word)
                top+=1
                word=""
                continue
            word+=s[i]
        st.append(word)
        top+=1
        ans=""
        while top>0:
            top-=1
            temp=st[top]
            ans+=temp
            if top>0:
                ans+=" "
        return ans
 {% endhighlight %}
