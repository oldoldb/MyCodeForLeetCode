---
layout: post
title: Longest Valid Parentheses
date: 2014-08-21 18:55:16
disqus: y
---

## 题意：
求一组括号中的最长括号匹配长度

## 要求：
无

## 思路：
记dp[i]为以i结尾的最长括号匹配长度，那么当j<i且s[j]==‘(“时，dp[i]=dp[j-1]+i-j+1
从左向右遍历
- s[i]=‘(‘，压栈
- s[i]=‘)‘，弹栈，更新dp[i]
维护一个最大值ans就好

## 更新：
总结leetcode堆栈题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int ans=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='(')
                st.push(i);
            else
            {
                st.pop();
                if(st.empty())
                    st.push(i);
                else
                    ans=max(ans,i-st.top());
            }
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        n=len(s)
        st=[0 for i in range(n)]
        top=0
        dp=[0 for i in range(n)]
        ans=0
        for i in range(n):
            if s[i]=='(':
                st[top]=i
                top+=1
            else:
                if top==0:
                    continue
                top-=1
                pos=st[top]
                if pos==0:
                    dp[i]=i-pos+1
                else:
                    dp[i]=dp[pos-1]+i-pos+1
                ans=max(ans,dp[i])
        return ans
 {% endhighlight %}
