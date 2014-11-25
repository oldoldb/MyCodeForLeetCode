---
layout: post
title: Longest Substring Without Repeating Characters
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求字符串中最长的没有重复字符出现的子串的长度

## 要求：


## 思路：
http://blog.csdn.net/pickless/article/details/9018575
学到的是python中取ASCII码用ord()

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans=0;
        int idx=-1;
        int location[256];
        memset(location,-1,sizeof(location));
        for(int i=0;i<s.length();i++)
        {
            if(location[s[i]]>idx)
            {
                idx=location[s[i]];
            }
            if(i-idx>ans)
            {
                ans=i-idx;
            }
            location[s[i]]=i;
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ans = 0
        idx = -1
        location = [-1 for x in range(256)]
        for i in range(len(s)):
            if location[ord(s[i])]>idx:
                idx = location[ord(s[i])]
            if i-idx > ans:
                ans = i - idx
            location[ord(s[i])] = i
        return ans
 {% endhighlight %}
