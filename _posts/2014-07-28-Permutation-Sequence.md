---
layout: post
title: Permutation Sequence
date: 2014-07-28 15:52:16
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

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string getPermutation(int n, int k) {
        int *temp=new int[n+1];
        temp[0]=1;
        for(int i=1;i<=n;i++)
        {
            temp[i]=temp[i-1]*i;
        }
        string str="";
        int *visit=new int[n+1];
        memset(visit,0,sizeof(int)*(n+1));
        for(int i=n;i>=1;i--)//从最高位开始枚举
        {
            for(int j=n;j>=1;j--)//从最大值开始枚举
            {
                if(!visit[j])
                {
                    int cnt=0;
                    for(int p=1;p<j;p++)//该值是第几个
                    {
                        if(!visit[p])
                        {
                            cnt++;
                        }
                    }
                    if(temp[i-1]*cnt<k)
                    {
                        k-=temp[i-1]*cnt;
                        str+=(j+'0');
                        visit[j]=1;
                        break;
                    }
                }
            }
        }
        delete []temp;
        delete []visit;
        return str;
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
