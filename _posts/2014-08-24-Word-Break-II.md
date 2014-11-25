---
layout: post
title: Word Break II
date: 2014-08-24 15:07:16
disqus: y
---

## 题意：
在Word Break的基础上输出单词组合

## 要求：


## 思路：
 先递推，dp[i] == true 表示 s 中前 i 个字符的串是符合要求的，枚举位置 i ，对于 i 枚举位置 j < i，如果 dp[j] == true且 j ~ i的串在字典中，则dp[i] = true。

同时对于这样的 j, i，record[i].push_back(j)，即在 i 位置的可行迭代表中增加位置 j。

完成site之后，从尾部倒着DFS过去就得到了所有串。

## 更新：
总结leetcode动态规划题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void wordBreakHelper(vector<vector<int> > &record,int pos,string s,string path,vector<string> &ans)
    {
        for(int i=0;i<record[pos].size();i++)
        {
            string sub=s.substr(pos,record[pos][i]-pos);
            string newpath=path+(pos==0?sub:" "+sub);
            if(record[pos][i]==s.length())
                ans.push_back(newpath);
            else
                wordBreakHelper(record,record[pos][i],s,newpath,ans);
        }
    }
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        int n=s.length();
        vector<vector<int> > record(n+1,vector<int>());
        for(int j=n;j>=0;j--)
        {
            if(j<n&&record[j].size()==0)
                continue;
            for(int i=j-1;i>=0;i--)
                if(dict.count(s.substr(i,j-i)))
                    record[i].push_back(j);
        }
        vector<string> ans;
        wordBreakHelper(record,0,s,"",ans);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        length=len(s)
        record=[[] for x in range(length+1)]
        dp=[False for x in range(length+1)]
        dp[0]=True
        for i in range(1,length+1):
            for j in range(i):
                if dp[j]==True and s[j:i] in dict:
                    record[i].append(j)
                    dp[i]=True
        return self.dfs(s,record,length)
    def dfs(self,s,record,pos):
        ans=[]
        for i in range(len(record[pos])):
            temp=[]
            ss=s[record[pos][i]:pos]
            if len(record[record[pos][i]])==0:
                ans.append(ss)
            else:
                temp=self.dfs(s,record,record[pos][i])
                for j in range(len(temp)):
                    ans.append(temp[j]+" "+ss)
        return ans
 {% endhighlight %}
