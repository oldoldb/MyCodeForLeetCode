---
layout: post
title: Longest Consecutive Sequence
date: 2014-08-23 16:05:16
disqus: y
---

## 题意：
求无序数组中的最大连续元素长度

## 要求：
O(n)复杂度

## 思路：
一开始开了Hash,但测试数据告诉我hash放不下
搜题解看到用map实现，但是map明显是O(nlogn)复杂度？
不懂
后来查到说python中dictionary的get item的平均时间复杂度为O(1)?
python代码是看的别人的题解

##　更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        map<int,int>mp;
        for(vector<int>::iterator it=num.begin();it!=num.end();it++)
            mp[*it]=1;
        int temp=1;
        int ans=1;
        for(map<int,int>::iterator it=mp.begin();it!=mp.end();it++)
            if(mp.count(it->first+1))
                temp++;
            else
            {
                ans=max(ans,temp);
                temp=1;
            }
        ans=max(ans,temp);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict={x:False for x in num}
        ans=-1
        for i in dict:
            if dict[i]==False:
                cur=i+1
                len1=0
                while cur in dict and dict[cur]==False:
                    len1+=1
                    dict[cur]=True
                    cur+=1
                cur=i-1
                len2=0
                while cur in dict and dict[cur]==False:
                    len2+=1
                    dict[cur]=True
                    cur-=1
                ans=max(ans,1+len1+len2)
        return ans
 {% endhighlight %}
