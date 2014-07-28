---
layout: post
title: Container With Most Water
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
n个整数代表(i,ai)与(i,0)之间的n条竖线，盛水面积定义位两条线间的距离与两条线较短高度的乘积，求最大盛水量

## 要求：


## 思路：
双指针，head和tail从数组两边向之间缩进，同时维护一个最大值ans,如果head的高度较小，那么说明要想获得更大的ans只能看下一个head，即head++，tail同理

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int maxArea(vector<int> &height) {
        int ans=0;
        for(int i=0,j=height.size()-1;i<j;)
        {
            int tempans=min(height[i],height[j])*(j-i);
            ans=max(ans,tempans);
            if(height[i]<height[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @return an integer
    def maxArea(self, height):
        head=0
        tail=len(height)-1
        ans=0
        while head<tail:
            tempans=min(height[head],height[tail])*(tail-head)
            ans=max(tempans,ans)
            if height[head]<height[tail]:
                head+=1
            else:
                tail-=1
        return ans
 {% endhighlight %}
