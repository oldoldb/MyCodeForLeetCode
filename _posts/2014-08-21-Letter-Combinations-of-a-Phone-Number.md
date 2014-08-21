---
layout: post
title: Letter Combinations of a Phone Number
date: 2014-08-21 12:18:16
disqus: y
---

## 题意：
输入数字串，输出对应的九宫格中的字母组合

## 要求：


## 思路：
深搜

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(vector<string> &ans,string cur,string digits,int pos,string model[])
    {
        if(pos==digits.length())
        {
            ans.push_back(cur);
            return ;
        }
        for(int i=0;i<model[digits[pos]-'0'].length();i++)
        {
            cur.push_back(model[digits[pos]-'0'][i]);
            dfs(ans,cur,digits,pos+1,model);
            cur.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        string model[10]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        dfs(ans,"",digits,0,model);
        return ans;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    moderStr = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        ans = []
        str = ""
        pos = 0
        self.solve(pos, str, ans, digits)
        return ans
    def solve(self,pos,str,ans,digits):
        if pos == len(digits):
            ans.append(str)
            return 
        for i in range(len(self.moderStr[int(digits[pos])-int('0')])):
            str+=self.moderStr[int(digits[pos])-int('0')][i]
            self.solve(pos+1,str,ans,digits)
            str = str[:-1]
 {% endhighlight %}
