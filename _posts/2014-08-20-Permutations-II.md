---
layout: post
title: Permutations II
date: 2014-08-20 18:52:16
disqus: y
---

## 题意：
求含重复数字的序列的全排列

## 要求：


## 思路：
普通方法会T
加一个剪纸
首先对序列排序
在进行搜索的时候如果当前数字和前一个数字相同，那么必须前一个数字使用过这个数字才可以使用

更新：
总结leetcode排列组合题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(int pos,vector<int>vec,vector<vector<int> >&ans,vector<int>&visit,vector<int>num)
    {
        if(pos==num.size())
        {
        //    sort(vec.begin(),vec.end());
        /*
            if(find(ans.begin(),ans.end(),vec)==ans.end())
            {
                ans.push_back(vec);
            }
            */
            ans.push_back(vec);
            return ;
        }
        for(int i=0;i<num.size();i++)
        {
            if(!visit[i])
            {
                if(i==0 || i!=0&&num[i]==num[i-1]&&visit[i-1] || i!=0&&num[i]!=num[i-1])
                {
                    visit[i]=1;
                    vec.push_back(num[i]);
                    dfs(pos+1,vec,ans,visit,num);
                    vec.pop_back();
                    visit[i]=0;
                }
            }
        }
    }
    vector<vector<int> > permuteUnique(vector<int> &num) {
        sort(num.begin(),num.end());
        vector<vector<int> >ans;
        vector<int>vec;
        vector<int>visit;
        visit.resize(num.size());
        dfs(0,vec,ans,visit,num);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
class Solution:
    def dfs(self,pos,vec,ans,num,visit):
        if pos==len(num):
            temp=vec[:]
            ans.append(temp)
            return 
        for i in range(len(num)):
            if visit[i]==0:
                if i==0 or i!=0 and num[i]==num[i-1] and visit[i-1] or i!=0 and num[i]!=num[i-1]:
                    visit[i]=1
                    vec.append(num[i])
                    self.dfs(pos+1,vec,ans,num,visit)
                    vec.pop()
                    visit[i]=0
                    
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        ans=[]
        vec=[]
        visit=[0 for i in range(len(num))]
        num.sort()
        self.dfs(0,vec,ans,num,visit)
        return ans
 {% endhighlight %}
