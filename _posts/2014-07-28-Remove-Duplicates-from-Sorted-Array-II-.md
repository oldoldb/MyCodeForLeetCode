---
layout: post
title: Remove Duplicates from Sorted Array II 
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
从有序数组中删除出现次数大于两次的元素

## 要求：


## 思路：
模拟就好

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if(n==0)
        {
            return 0; 
        }
        int pos=1;
        int num=1;
        int last=A[0];
        for(int i=1;i<n;i++)
        {
            if(A[i]!=last)
            {
                A[pos++]=A[i];
                num=1;
                last=A[i];
            }
            else
            {
                if(num==2)
                {
                    continue;
                    
                }
                else
                {
                    A[pos++]=last;
                    num++;
                }
            }
        }
        return pos;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0:
            return 0
        pos=1
        num=1
        last=A[0]
        for i in range(1,len(A)):
            if A[i]!=last:
                A[pos]=A[i]
                pos+=1
                last=A[i]
                num=1
            elif num==2:
                continue
            else:
                num+=1
                A[pos]=last
                pos+=1
        return pos
 {% endhighlight %}
