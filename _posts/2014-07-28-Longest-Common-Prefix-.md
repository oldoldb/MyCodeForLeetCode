---
layout: post
title: Longest Common Prefix 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求字符串数组的最长公共前缀

## 要求：
无

## 思路：
先查找长度最短的字符串，在一位一位的比较？
只能想到这么朴素的方法
高级数据结构不会。

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if(strs.size()==0)
        {
            return "";
        }
        int mark=0;
        int minlen=10000;
        for(int i=0;i<strs.size();i++)
        {
            if(strs[i].length()<minlen)
            {
                mark=i;
                minlen=strs[i].length();
            }
        }
        string ans="";
        for(int i=0;i<strs[mark].length();i++)
        {
            for(int j=0;j<strs.size();j++)
            {
                if(strs[j][i]!=strs[mark][i])
                {
                    return ans;
                }
            }
            ans+=strs[mark][i];
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        minlen=10000
        mark=0
        for i in range(len(strs)):
            if len(strs[i])<minlen:
                minlen=len(strs[i])
                mark=i
        ans=""
        for i in range(len(strs[mark])):
            for j in range(len(strs)):
                if strs[j][i]!=strs[mark][i]:
                    return ans
            ans+=strs[mark][i]
        return ans
 {% endhighlight %}
