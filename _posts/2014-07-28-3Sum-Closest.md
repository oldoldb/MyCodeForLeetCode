---
layout: post
title: 3Sum Closest
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
给一个n个元素的数组，求其中三个元素的和，使其最接近Target

## 要求：


## 思路：
类似2Sum的思想，先排序，然后枚举第一个元素的位置，对另外两个元素进行2Sum

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        sort(num.begin(),num.end());
        int n=num.size();
        bool flag=true;
        int ans;
        for(int i=0;i<n;i++)
        {
            int start=i+1;
            int end=n-1;
            while(start<end)
            {
                int temp=num[i]+num[start]+num[end];
                if(flag)
                {
                    ans=temp;
                    flag=false;
                }
                if(abs(temp-target)<abs(ans-target))
                {
                    ans=temp;
                }
                if(ans==target)
                {
                    return ans;
                }
                else if(temp<target)
                {
                    start++;
                }
                else
                {
                    end--;
                }
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
    def threeSumClosest(self, num, target):
        num.sort()
        first=True
        for i in range(len(num)):
            start=i+1
            end=len(num)-1
            while start<end:
                temp=num[i]+num[start]+num[end]
                if first:
                    ans=temp
                    first=False
                if abs(temp-target)<abs(ans-target):
                    ans=temp
                if target==temp:
                    return ans
                elif temp<target:
                    start+=1
                else:
                    end-=1
        return ans
 {% endhighlight %}
