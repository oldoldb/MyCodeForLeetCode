---
layout: post
title: Generate Parentheses
date: 2014-08-20 11:16:16
disqus: y
---

## 题意：
给定n，生成n个括号所有合法序列

## 要求：


## 思路：
深搜

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        stack<string> st;
        st.push("(");
        stack<int> num;
        num.push(0);
        while(!st.empty())
        {
            string str=st.top();
            st.pop();
            int temp=num.top();
            num.pop();
            if(str.length()==n*2)
            {
                ans.push_back(str);
                continue;
            }
            if(str.length()-temp<n)
            {
                st.push(str+"(");
                num.push(temp);
            }
            if(str.length()>temp*2)
            {
                st.push(str+")");
                num.push(temp+1);
            }
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    def dfs(self,lpos,rpos,n,ans,str):
        if rpos>lpos or lpos>n and rpos>n:
            return 
        if lpos==n and rpos==n:
            ans.append(str)
            return 
        if lpos<n:
            temp=str[:]
            temp+='('
            self.dfs(lpos+1,rpos,n,ans,temp)
        if rpos<n:
            temp=str[:]
            temp+=')'
            self.dfs(lpos,rpos+1,n,ans,temp)
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ans=[]
        str=""
        self.dfs(0,0,n,ans,str)
        return ans
 {% endhighlight %}
