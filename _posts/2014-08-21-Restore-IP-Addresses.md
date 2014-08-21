---
layout: post
title: Restore IP Addresses
date: 2014-08-21 13:31:16
disqus: y
---

## 题意：
将一个字符串转换成所有可能的IP地址形式

## 要求：
无

## 思路：
深搜，注意剪枝
这里C++方法参照了《手写代码必备手册》
python方法参照了http://chaoren.is-programmer.com/posts/42718.html
递归方法，str(int(s)) == s是为了去掉前导0，即Input＝"010010"时, Output不能是"0.1.0.010"之类的。

## 更新：
总结leetcode回溯题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    bool ok(string str)
    {
        if(str.size()>1 && str[0]=='0')  
            return false;
        if(stoi(str)>255 || stoi(str)<0)
            return false;
        return true;
    }
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        int n=s.length();
        if(n>12 || n<4)
            return ans;
        for(int i=1;i<4;i++)
        {
            string first=s.substr(0,i);
            if(!ok(first))
                continue;
            for(int j=1;j<4 && i+j<n;j++)
            {
                string second=s.substr(i,j);
                if(!ok(second))
                    continue;
                for(int k=1;k<4 && i+j+k<n;k++)
                {
                    string third=s.substr(i+j,k);
                    string fourth=s.substr(i+j+k);
                    if(!ok(third) || !ok(fourth))
                        continue;
                    ans.push_back(first+"."+second+"."+third+"."+fourth);
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
    # @param s, a string
    # @return a list of strings
 
    def getIP(self, currIP, s, currIndex):
        if currIndex == 3:
            if len(s) > 0:
                if str(int(s)) == s and int(s) <= 255:
                    Solution.res.append(currIP + s)
            return
        length = len(s)
        for i in xrange(1,4):
            if length >= i and str(int(s[0:i])) == s[0:i] and int(s[0:i]) <= 255:
                self.getIP(currIP + s[0:i] + '.', s[i:], currIndex + 1)
        return
 
    def restoreIpAddresses(self, s):
        Solution.res = []
        self.getIP('', s, 0)
        return Solution.res
 {% endhighlight %}
