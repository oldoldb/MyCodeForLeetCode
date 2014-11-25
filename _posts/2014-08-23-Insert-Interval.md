---
layout: post
title: Insert Interval
date: 2014-08-23 13:47:16
disqus: y
---

## 题意：
将新区间插入到有序的区间中

## 要求：


## 思路：
如果新区间的end < 当前区间的start，不用找下去了，把新区间插入到当前区间的前面，然后返回。
如果当前区间的end小于新区间的start，继续遍历找下一个区间。
如果当前区间和新区间发生重合，则start取两者最小的start，end取两者最大的end，生成一个新的区间。
继续遍历。

如果遍历一直到末尾也没发生区间重合，就把新区间插入到原来ArrayList的末尾。

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
class Solution {
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        vector<Interval> ans;
        int size=intervals.size();
        for(int i=0;i<size;i++)
            if(newInterval.start>intervals[i].end)
                ans.push_back(intervals[i]);
            else if(newInterval.end<intervals[i].start)
            {
                ans.push_back(newInterval);
                ans.insert(ans.end(),intervals.begin()+i,intervals.end());
                return ans;
            }
            else
            {
                newInterval.start=min(newInterval.start,intervals[i].start);
                newInterval.end=max(newInterval.end,intervals[i].end);
            }
        ans.push_back(newInterval);
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
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        ans=[]
        size = len(intervals)
        for i in range(size):
            if newInterval.start>intervals[i].end:
                ans.append(intervals[i])
            elif newInterval.end<intervals[i].start:
                ans.append(newInterval)
                ans+=intervals[i:]
                return ans
            else:
                newInterval.start=min(newInterval.start,intervals[i].start)
                newInterval.end=max(newInterval.end,intervals[i].end)
        ans.append(newInterval)
        return ans
 {% endhighlight %}
