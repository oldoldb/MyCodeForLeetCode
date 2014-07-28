---
layout: post
title: Minimum Window Substring
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
在S中寻找包含全部T中字符的最短子串

## 要求：


## 思路：
http://www.cnblogs.com/lichen782/p/leetcode_minimum_window_substring_3.html

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string minWindow(string S, string T) {
        int lent=T.length();
        int lens=S.length();
        int needToFind[256]={0};
        for(int i=0;i<lent;i++)
        {
            needToFind[T[i]]++;
        }
        int hasFound[256]={0};
        int minBegin;
        int minEnd;
        int minWindow=lens+1;
        int cnt=0;
        char ch;
        for(int begin=0,end=0;end<lens;end++)
        {
            if(needToFind[S[end]]==0)
            {
                continue;
            }
            ch=S[end];
            hasFound[ch]++;
            if(hasFound[ch]<=needToFind[ch])
            {
                cnt++;
            }
            if(cnt==lent)
            {
                while(needToFind[S[begin]]==0 || hasFound[S[begin]]>needToFind[S[begin]])
                {
                    if(hasFound[S[begin]]>needToFind[S[begin]])
                    {
                        hasFound[S[begin]]--;
                    }
                    begin++;
                }
                int length=end-begin+1;
                if(length<minWindow)
                {
                    minWindow=length;
                    minBegin=begin;
                    minEnd=end;
                }
            }
        }
        return minWindow<=lens?S.substr(minBegin,minEnd-minBegin+1):"";
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a string
    def minWindow(self, S, T):
        lent=len(T)
        lens=len(S)
        needToFind=[0 for x in range(256)]
        for i in range(lent):
            needToFind[ord(T[i])]+=1
        hasFound=[0 for x in range(256)]
        minBegin=0
        minEnd=0
        minWindow=lens+1
        cnt=0
        begin=0
        for end in range(lens):
            if needToFind[ord(S[end])]==0:
                continue
            ch=ord(S[end])
            hasFound[ch]+=1
            if hasFound[ch]<=needToFind[ch]:
                cnt+=1
            if cnt==lent:
                while needToFind[ord(S[begin])]==0 or hasFound[ord(S[begin])]>needToFind[ord(S[begin])]:
                    if hasFound[ord(S[begin])]>needToFind[ord(S[begin])]:
                        hasFound[ord(S[begin])]-=1
                    begin+=1
                length=end-begin+1
                if length<minWindow:
                    minWindow=length
                    minBegin=begin
                    minEnd=end
        return S[minBegin:minEnd+1] if minWindow<=lens else ""
 {% endhighlight %}
