---
layout: post
title: Valid Palindrome
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
判断string是不是回文串，只需判断字母和数字

## 要求：
字母不区分大小写

## 思路：
首尾两个指针扫一遍就行

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isPalindrome(string s) {
        if(s=="")
        {
            return true;
        }
        int p=0;
        int q=s.length()-1;
        while(p<q)
        {
            while(!isalpha(s[p]) && !isdigit(s[p]) && p<q)
            {
                p++;
            }
            while(!isalpha(s[q]) && !isdigit(s[q]) && q>p)
            {
                q--;
            }
            if(p>=q)
            {
                return true;
            }
            if(isalpha(s[p]) && isalpha(s[q]))
            {
                if(toupper(s[p])!=toupper(s[q]))
                {
                    return false;
                }
                else
                {
                    p++;
                    q--;
                }
            }
            else if(s[p]==s[q])
            {
                p++;
                q--;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        p = 0
        q = len(s) - 1
        while p < q:
            while not s[p].isalpha() and not s[p].isdigit() and p<q:
                p = p + 1
            while not s[q].isalpha() and not s[q].isdigit() and p<q:
                q = q - 1
            if p>=q:
                return True
            if s[p].isalpha() and s[q].isalpha():
                if s[p].upper()!=s[q].upper():
                    return False
                else:
                    p = p + 1
                    q = q - 1
            elif s[p] == s[q]:
                p = p + 1
                q = q - 1
            else:
                return False
        return True
 {% endhighlight %}
