---
layout: post
title: Merge Intervals
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给出区间集合，合并所有区间

## 要求：


## 思路：
http://blog.csdn.net/pickless/article/details/9921011
http://blog.csdn.net/perfect8886/article/details/21783299

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
public:
    vector<Interval> merge(vector<Interval> &intervals) {
        vector<Interval>ans;
        if(intervals.empty())
        {
            return ans;
        }
        int MIN=INT_MAX;
        int MAX=INT_MIN;
        for(int i=0;i<intervals.size();i++)
        {
            MIN=min(MIN,intervals[i].start);
            MAX=max(MAX,intervals[i].end);
        }
        int left[MAX-MIN+1];
        int right[MAX-MIN+1];
        memset(left,0,sizeof(left));
        memset(right,0,sizeof(right));
        for(int i=0;i<intervals.size();i++)
        {
            left[intervals[i].start-MIN]++;
            right[intervals[i].end-MIN]++;
        }
        int start=-1;
        int cnt=0;
        for(int i=0;i<MAX-MIN+1;i++)
        {
            cnt+=left[i];
            if(cnt>0&&start==-1)
            {
                start=i;
            }
            cnt-=right[i];
            if(cnt==0&&start!=-1)
            {
                ans.push_back(Interval(start+MIN,i+MIN));
                start=-1;
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
