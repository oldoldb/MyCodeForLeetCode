---
layout: post
title: Single Number II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
从每个元素都出现三次的数组中找出只出现一次的元素

## 要求：
线性时间复杂度
不适用额外空间

## 思路：
扫一遍数组，可以统计出每一位出现的次数，每位出现次数模3余1所得到的数就是只出现一次的数，这样开一个32位的数组表示每位出现的个数就可以

要做到不使用额外空间，网上搜了题解，只有一个讲的还比较清楚
类似自动机的思想，给三个量ones,twos,threes分别记录只出现一次、两次、三次的数，同时扫一遍数组的时候更新每个量，最终只出现一次的数就是ones

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int singleNumber(int A[], int n) {
        int ones=0;
        int twos=0;
        int threes=0;
        for(int i=0;i<n;i++)
        {
            threes=twos & A[i];//已经出现两次并且再次出现
            twos=twos | ones & A[i];//曾经出现两次的或者曾经出现一次但是再次出现的
            ones=ones | A[i];//出现一次的
            twos=twos & ~threes;//当某一位出现三次后，就从出现两次中消去
            ones=ones & ~threes;//当某一位出现三次后，就从出现一次中消去
        }
        return ones;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones=0
        twos=0
        threes=0
        for i in range(len(A)):
            threes=twos & A[i]
            twos = twos | ones & A[i]
            ones = ones | A[i]
            twos= twos & ~threes
            ones =ones & ~threes
        return ones
 {% endhighlight %}
