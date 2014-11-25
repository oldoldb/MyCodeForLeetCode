---
layout: post
title: Restore IP Addresses
date: 2014-07-28 15:52:16
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
## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    void dfs(string s,int pos,int step,string ip,vector<string> &ans)
    {
        int n=s.length();
        if(n-pos>(4-step)*3)//剩下的太多
        {
            return ;
        }
        if(n-pos<4-step)//剩下的不够
        {
            return ;
        }
        if(pos==n&&step==4)
        {
            ip.resize(ip.size()-1);//去掉末尾多余的'.'
            ans.push_back(ip);
            return ;
        }
        int num=0;
        for(int i=pos;i<pos+3;i++)
        {
            num=num*10+s[i]-'0';
            if(num<=255)
            {
                ip+=s[i];
                dfs(s,i+1,step+1,ip+'.',ans);
            }
            if(num==0)
            {
                break;
            }
        }
    }
    vector<string> restoreIpAddresses(string s) {
        vector<string>ans;
        string ip;
        dfs(s,0,0,ip,ans);
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
