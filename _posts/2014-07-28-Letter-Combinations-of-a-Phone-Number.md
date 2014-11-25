---
layout: post
title: Letter Combinations of a Phone Number
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
输入数字串，输出对应的九宫格中的字母组合

## 要求：


## 思路：
深搜

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    string modelStr[10]={"","","abc","def","ghi","jkl","mno","qprs","tuv","wxzy"};
    void solve(int pos, string str, vector<string>& ans, string digits)
    {
        if(pos==digits.length())
        {
            ans.push_back(str);
            return ;
        }
        for(int i=0;i<modelStr[digits[pos]-'0'].length();i++)
        {
            str.push_back(modelStr[digits[pos]-'0'][i]);
            solve(pos+1,str,ans,digits);
            str.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        int pos = 0;
        string str;
        solve(pos, str, ans, digits);
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
