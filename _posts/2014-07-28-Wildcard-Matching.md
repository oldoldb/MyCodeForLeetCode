---
layout: post
title: Wildcard Matching
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
另一种形式的正则匹配

## 要求：


## 思路：
http://www.cnblogs.com/x1957/p/3517096.html

我们来匹配s和p

如果匹配就s++ , p++

如果不匹配的话就看p之前知否有*

当然是否有*我们需要记录的,遇到*就记录当前*的位置和匹配到的s的位置

然后从*的下一位置匹配,开始匹配0个字符

如果ok往后走,往后不ok,那么匹配1个字符...同理2,3,4个字符(有点回溯的感觉吧

所以实践复杂度是O(len(s) * len(p))


python做法：
http://chaoren.is-programmer.com/posts/42771.html

遇到'*'时, 用star变量记录'*'在p中出现的位置, 用ss变量记录此时s字符串指针sPointer的位置, 但不移动sPointer, 因为'*'可以匹配0个字符, ss表示这个'*'所能匹配到的位置。遇到不匹配的情况时, 即走到if star!= -1时, pPointer被拉回到star的下一个位置, sPointer被拉回到ss的下一个位置, 继续匹配。把s字符串走完, p中还可以剩下一堆'*', 如果p中还有其他字符就返回False了。
## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        //? match one
        //* match 0,1,2,3..
        // aaaabc *c true
        const char* star = nullptr;
        const char* rs = nullptr;
        
        while(*s) {
            if(*s == *p || *p == '?') { //match
                s++; p++;
                continue;
            }
            if(*p == '*') { 
                star = p; // record star
                p++; //match from next p
                rs = s; // record the position of s , star match 0
                continue;
            } 
            if(star != nullptr) { //if have star in front then backtrace
                p = star + 1; //reset the position of p 
                s = rs + 1; 
                rs ++; //star match 1,2,3,4,5....
                continue;
            }
            return false; //if not match return false
        }
        while(*p == '*') p++; //skip continue star
        return *p == '\0'; // successful match
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        len_s = len(s); len_p = len(p)
        pPointer = sPointer = ss = 0
        star = -1
        while sPointer < len_s:
            if pPointer < len_p and (p[pPointer] == '?' or p[pPointer] == s[sPointer]):
                sPointer += 1; pPointer += 1;
                continue
            if pPointer < len_p and p[pPointer] == '*':
                star = pPointer; pPointer +=1; ss = sPointer
                continue
            if star != -1:
                pPointer = star + 1; ss += 1; sPointer = ss
                continue
            return False
        while pPointer < len_p and p[pPointer] == '*':
            pPointer += 1
        return pPointer == len_p
 {% endhighlight %}
