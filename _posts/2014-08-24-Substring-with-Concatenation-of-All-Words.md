---
layout: post
title: Substring with Concatenation of All Words
date: 2014-08-24 16:12:16
disqus: y
---

## 题意：
满足全部包含L中单词且中间无其他干扰项，返回这样的条件的开头和结尾索引

## 要求：


## 思路：
http://www.cnblogs.com/awy-blog/p/3821586.html
这道题意思是说满足全部包含L中单词且中间无其他干扰项，返回这样的条件的开头和结尾索引。这道题主要使用map数据结构来解题，主要是使用map来记录L中单词出现的次数。循环遍历字符串，找出存在与L中的字符串且L中单词必须连续、全部出现。查找某个单词成功后将这个单词加入到新的map容器中，这个容器存储的是从当前指针位置开始满足单词列表的单词，同时统计次数，接下来如果这个但是在新容器出现的次数是否小于等初始化容器的次数。如果大于，则是错误的，指针后移。然后在找出其他L中的单词。(注意L中单词必须连续出现)最后我们后移单词列表中指定个数的单词或者因为不匹配而终止从指针位置i开始，如果查找成功就把当前指针的位置记录下来。如此找出所有满足条件的情况。

## 更新：
总结leetcode字符串题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<int> findSubstring(string S, vector<string> &L) {
        vector<int>ans;
        int n=L.size();
        if(n==0)
            return ans;
        int len=L[0].length();
        int lens=S.length();
        if(lens==0)
            return ans;
        map<string,int>words,cur;
        for(int i=0;i<n;i++)
            words[L[i]]++;
        for(int i=0;i<=(lens-n*len);i++)
        {
            cur.clear();
            int j=0;
            for( ;j<n;j++)
            {
                string temp=S.substr(i+j*len,len);
                if(words.find(temp)==words.end())
                    break;
                cur[temp]++;
                if(words[temp]<cur[temp])
                    break;
            }
            if(j==n)
                ans.push_back(i);
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        ans=[]
        n=len(L)
        if n==0:
            return ans
        wordlen=len(L[0])
        lens=len(S)
        if lens==0:
            return ans
        dict={}
        cur={}
        for i in range(n):
            if L[i] in dict:
                dict[L[i]]+=1
            else:
                dict[L[i]]=1
        for i in range(lens-n*wordlen+1):
            cur.clear()
            j=0
            while j<n:
                temp=S[i+j*wordlen:i+j*wordlen+wordlen]
                if temp not in dict:
                    break
                if temp in cur:
                    cur[temp]+=1
                else:
                    cur[temp]=1
                if dict[temp]<cur[temp]:
                    break
                j+=1
            if j==n:
                ans.append(i)
        return ans
 {% endhighlight %}
