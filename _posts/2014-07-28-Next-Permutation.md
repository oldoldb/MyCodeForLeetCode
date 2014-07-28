---
layout: post
title: Next Permutation
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求一个排列

## 要求：
无

## 思路：
求下一个排列的算法如下：
示例6	8	7	4	3	2
- 从右向左，找到第一个破坏递增趋势的数，例如例子中的6，记录它的下标0
- 从右向左，找到第一个比6大的数，例如例子中的7，记录它的下标2
- 交换下标0和2的值，即swap(num[0],num[2])，序列变成7	8	6	4	3	2
- 反转7右边的所有数，即reverse(num.begin()+1,num.end())，得到7	2	3	4	6	8

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void nextPermutation(vector<int> &num) {
        int n=num.size();
        int mark=-1;
        for(int i=n-1;i>0;i--)
        {
            if(num[i]<=num[i-1])
            {
                continue;
            }
            else
            {
                mark=i-1;
                break;
            }
        }
        if(mark==-1)
        {
            reverse(num.begin(),num.end());
            return ;
        }
        int mark2=0;
        for(int i=n-1;i>mark;i--)
        {
            if(num[i]>num[mark])
            {
                mark2=i;
                break;
            }
        }
        swap(num[mark],num[mark2]);
        reverse(num.begin()+mark+1,num.end());
        return ;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n=len(num)
        mark=-1
        for i in range(n-1,0,-1):
            if num[i]<=num[i-1]:
                continue
            else:
                mark=i-1
                break
        if mark==-1:
            num.reverse()
            return num
        for i in range(n-1,mark,-1):
            if num[i]>num[mark]:
                mark2=i
                break
        num[mark],num[mark2]=num[mark2],num[mark]
        num2=num[mark+1:]
        num2.reverse()
        for i in range(mark+1,n):
            num[i]=num2[i-mark-1]
        return num
 {% endhighlight %}
