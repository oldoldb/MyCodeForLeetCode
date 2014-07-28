---
layout: post
title: Scramble String
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
判断两个string是不是Scramble string

## 要求：


## 思路：
http://www.blogjava.net/sandy/archive/2013/05/22/399605.html
http://blog.csdn.net/pickless/article/details/11501443

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1.length()!=s2.length())
        {
            return false;
        }
        if(s1.length()==0)
        {
            return true;
        }
        bool ans[100][100][100]={false};
        for(int i=0;i<s1.length();i++)
        {
            for(int j=0;j<s1.length();j++)
            {
                ans[0][i][j]=(s1[i]==s2[j]);
            }
        }
        for(int k=2;k<=s1.length();k++)
        {
            for(int i=s1.length()-k;i>=0;i--)
            {
                for(int j=s1.length()-k;j>=0;j--)
                {
                    bool flag = false;
                    for(int m=1;m<k&&!flag;m++)
                    {
                        flag=ans[m-1][i][j]&&ans[k-m-1][i+m][j+m] || ans[m-1][i][j+k-m]&&ans[k-m-1][i+m][j];
                    }
                    ans[k-1][i][j]=flag;
                }
            }
        }
        return ans[s1.length()-1][0][0];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1)==0:
            return True
        lens1 = len(s1)
        ans = [[[0 for x in range(lens1)] for y in range(lens1)]for z in range(lens1)]
        for i in range(lens1):
            for j in range(len(s1)):
                ans[0][i][j] = (s1[i]==s2[j])
        for k in range(2,lens1+1):
            for i in range(lens1-k,-1,-1):
                for j in range(lens1-k,-1,-1):
                    flag = False;
                    for m in range(1,k):
                        if flag==True:
                            break
                        flag= ans[m-1][i][j] and ans[k-m-1][i+m][j+m] or ans[m-1][i][j+k-m] and ans[k-m-1][i+m][j]
                    ans[k-1][i][j]=flag
        return ans[lens1-1][0][0]
 {% endhighlight %}
