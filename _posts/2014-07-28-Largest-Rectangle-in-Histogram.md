---
layout: post
title: Largest Rectangle in Histogram
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求最大直方图面积

## 要求：


## 思路：
维护一个栈

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        int size=height.size();
        if(size==0)
        {
            return 0;
        }
        stack<int>s;
        height.push_back(0);
        int sum=0;
        for(int i=0;i<height.size();i++)
        {
            if(s.empty()||height[i]>height[s.top()])
            {
                s.push(i);
            }
            else
            {
                int temp=s.top();
                s.pop();
                sum=max(sum,height[temp]*(s.empty()?i:i-s.top()-1));
                i--;
            }
        }
        return sum;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        size=len(height)
        if size==0:
            return 0
        sum=0
        s=[]
        height.append(0)
        size+=1
        i=0
        while i<size:
            if len(s)==0 or height[i]>height[s[-1]]:
                s.append(i)
            else:
                temp=s[-1]
                s.pop(-1)
                sum=max(sum,height[temp]*(i if len(s)==0 else i-s[-1]-1))
                i=i-1
            i=i+1
        return sum
        
 {% endhighlight %}
