---
layout: post
title: Pascal's Triangle
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
求Pascal’s Triangle

## 要求：
无

## 思路：
dp[i][j]=dp[i-1][j]+dp[i-1][j-1]

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> >ans;
        ans.resize(numRows);
        for(int i=0;i<numRows;i++)
        {
            for(int j=0;j<=i;j++)
            {
                if(j==0||j==i)
                {
                    ans[i].push_back(1);
                }
                else
                {
                    ans[i].push_back(ans[i-1][j]+ans[i-1][j-1]);
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
    # @return a list of lists of integers
    def generate(self, numRows):
        ans=[[] for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j==i:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j]+ans[i-1][j-1])
        return ans
 {% endhighlight %}
