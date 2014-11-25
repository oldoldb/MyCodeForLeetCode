---
layout: post
title: Reverse Words in a String
date: 2014-08-13 19:29:16
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

## 更新 8/13/2014:
今天在discuss中发现以前的办法好蠢。。c++和Python明明都有更巧妙的解决方法

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void reverseWords(string &s) {
        string ans;
        for(int i=s.length()-1;i>=0; )
        {
            while(i>=0 && s[i]==' ')
                i--;
            if(i<0)
                break;
            if(!ans.empty())
                ans.push_back(' ');
            string temp;
            while(i>=0 && s[i]!=' ')
                temp.push_back(s[i--]);
            reverse(temp.begin(),temp.end());
            ans.append(temp);
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
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))
 {% endhighlight %}
