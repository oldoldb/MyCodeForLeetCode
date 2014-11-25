---
layout: post
title: Max Points on a Line
date: 2014-08-23 15:36:16
disqus: y
---

## 题意：
给定n个点，求在一条直线上的点的最大个数

## 要求：


## 思路：

http://blog.csdn.net/doc_sgl/article/details/17103427
任意一条直线都可以表述为

y = ax + b

假设，有两个点(x1,y1), (x2,y2)，如果他们都在这条直线上则有

y1 = kx1 +b

y2 = kx2 +b

由此可以得到关系，k = (y2-y1)/(x2-x1)。即如果点c和点a的斜率为k, 而点b和点a的斜率也为k，可以知道点c和点b也在一条线上。

取定一个点points[i], 遍历其他所有节点, 然后统计斜率相同的点数，并求取最大值即可

## 更新：
总结leetcode数学题目

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        unordered_map<float,int>mp;
        int ans=0;
        for(int i=0;i<points.size();i++)
        {
            mp.clear();
            mp[INT_MIN]=0;
            int cnt=1;
            for(int j=0;j<points.size();j++)
            {
                if(j==i)
                    continue;
                if(points[i].x==points[j].x && points[i].y==points[j].y)
                {
                    cnt++;
                    continue;
                }
                float k=points[i].x==points[j].x?INT_MAX:(float)(points[j].y-points[i].y)/(points[j].x-points[i].x);
                mp[k]++;
            }
            unordered_map<float,int>::iterator it=mp.begin();
            for( ;it!=mp.end();it++)
                ans=max(ans,it->second+cnt);
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        length=len(points)
        if length<3:
            return length
        ans=-1
        for i in range(length):
            slope={'int':0}
            cnt=1
            for j in range(length):
                if i==j:
                    continue;
                if points[i].x==points[j].x and points[i].y!=points[j].y:
                    slope['int']+=1
                elif points[i].x!=points[j].x:
                    k=1.0*(points[i].y-points[j].y)/(points[i].x-points[j].x)
                    slope[k]=1 if k not in slope else slope[k]+1
                else:
                    cnt+=1
            ans=max(ans,max(slope.values())+cnt)
        return ans
 {% endhighlight %}
