---
layout: post
title: Merge Intervals
date: 2014-08-23 13:43:16
disqus: y
---

## 题意：
给出区间集合，合并所有区间

## 要求：


## 思路：
http://blog.csdn.net/pickless/article/details/9921011
http://blog.csdn.net/perfect8886/article/details/21783299

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
bool cmp(const Interval &x,const Interval &y)
{
    return x.start<y.start;
}
class Solution {
public:
    vector<Interval> merge(vector<Interval> &intervals) {
        vector<Interval> ans;
        sort(intervals.begin(),intervals.end(),cmp);
        for(int i=0;i<intervals.size();i++)
        {
            if(i==0)
                ans.push_back(intervals[i]);
            else
            {
                int size=ans.size();
                if(ans[size-1].end>=intervals[i].start)
                    ans[size-1].end=max(ans[size-1].end,intervals[i].end);
                else
                    ans.push_back(intervals[i]);
            }
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals==None or len(intervals)==0:
            return intervals
        n=len(intervals)
        ans=[]
        intervals = sorted(intervals,cmp=lambda x,y : cmp(x.start,y.start))
        temp = intervals[0]
        for i in range(1,n):
            if temp.end<intervals[i].start:
                ans.append(temp)
                temp=intervals[i]
            else:
                temp.end=max(temp.end,intervals[i].end)
        ans.append(temp)
        return ans
 {% endhighlight %}
