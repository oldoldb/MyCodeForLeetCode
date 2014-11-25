---
layout: post
title: Permutation Sequence
date: 2014-08-20 19:30:16
disqus: y
---

## 题意：
给定n和k，求第K个全排列

## 要求：


## 思路：
暴力深搜就算了吧
这里考虑数学的解法
从最高位开始遍历
	数字从大到小开始枚举
		判断以当前数字在该位置时最少应为第几个排列

## 更新：
总结leetcode排列组合题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string getPermutation(int n, int k) {
        string ans="";
        vector<int> fac(n+1,1);
        vector<char> num(n,'1');
        for(int i=2;i<=n;i++)
        {
            fac[i]=fac[i-1]*i;
            num[i-1]=i+'0';
        }
        k--;
        for(int i=n-1;i>=0;i--)
        {
            int cur=k/fac[i];
            k%=fac[i];
            ans+=num[cur];
            num.erase(num.begin()+cur);
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        temp=[]
        temp.append(1)
        for i in range(1,n+1):
            temp.append(temp[i-1]*i)
        ans=""
        visit=[0 for i in range(n+1)]
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                if visit[j]==0:
                    cnt=0
                    for q in range(1,j):
                        if visit[q]==0:
                            cnt+=1
                    if temp[i-1]*cnt<k:
                        k-=temp[i-1]*cnt
                        ans+=str(j+int('0'))
                        visit[j]=1
                        break
        return ans
 {% endhighlight %}
