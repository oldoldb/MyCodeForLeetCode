---
layout: post
title: Word Break II
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
在Word Break的基础上输出单词组合

## 要求：


## 思路：
 先递推，dp[i] == true 表示 s 中前 i 个字符的串是符合要求的，枚举位置 i ，对于 i 枚举位置 j < i，如果 dp[j] == true且 j ~ i的串在字典中，则dp[i] = true。

同时对于这样的 j, i，record[i].push_back(j)，即在 i 位置的可行迭代表中增加位置 j。

完成site之后，从尾部倒着DFS过去就得到了所有串。

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    vector<string> dfs(string s,vector<int> *record,int pos)
    {
        vector<string>ans;
        for(int i=0;i<record[pos].size();i++)
        {
            vector<string>temp;
            string str=s.substr(record[pos][i],pos-record[pos][i]);
            if(record[record[pos][i]].size()==0)
            {
                ans.push_back(str);
            }
            else
            {
                temp=dfs(s,record,record[pos][i]);
                for(int j=0;j<temp.size();j++)
                {
                    ans.push_back(temp[j]+" "+str);
                }
            }
        }
        return ans;
    }
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        int length=s.length();
        vector<int> *record=new vector<int>[length+1];
        bool *dp=new bool[length+1];
        memset(dp,0,sizeof(bool)*length);
        dp[0]=true;
        for(int i=1;i<=length;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(dp[j]==true && dict.count(s.substr(j,i-j)))
                {
                    record[i].push_back(j);
                    dp[i]=true;
                }
            }
        }
        return dfs(s,record,length);
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
