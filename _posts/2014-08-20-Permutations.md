---
layout: post
title: Permutations
date: 2014-08-20 18:13:16
disqus: y
---

## 题意：
求给定数组的全排列
## 要求：
无

## 思路：
题目限制了返回类型必须是vector<vector<int> >，这就必须传递引用了
采用了生成全排列的经典算法交换元素的方法

这里需要注意的一点，我用python实现的时候，
if pos==n:
            temp=tempans[:]
            ans.append(temp)
这里如果直接ans.append(tympans)，会导致最后的ans列表中都是空列表项，这是由于Python特殊的参数传递的方式导致的（具体？）
所以这里我将tempans首先复制一下，同样不能单纯的用”=“复制，这样只会增加一个指针，而采用切片的方法

## 更新：
总结leetcode排列组合题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(vector<vector<int> > &ans,vector<int> &num,int pos)
    {
        if(pos==num.size())
            ans.push_back(num);
        for(int i=pos;i<num.size();i++)
        {
            swap(num[pos],num[i]);
            dfs(ans,num,pos+1);
            swap(num[pos],num[i]);
        }
    }
    vector<vector<int> > permute(vector<int> &num) {
        vector<vector<int> >ans;
        dfs(ans,num,0);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    def dfs(self,pos,num,ans,tempans):
        n=len(num)
        if pos==n:
            temp=tempans[:]
            ans.append(temp)
        for i in range(pos,n):
            num[pos],num[i]=num[i],num[pos]
            tempans.append(num[pos])
            self.dfs(pos+1,num,ans,tempans)
            tempans.pop()
            num[pos],num[i]=num[i],num[pos]
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        ans=[]
        tempans=[]
        self.dfs(0,num,ans,tempans)
        return ans
 {% endhighlight %}
