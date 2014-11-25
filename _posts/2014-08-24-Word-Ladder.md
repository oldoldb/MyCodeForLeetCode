---
layout: post
title: Word Ladder
date: 2014-08-24 15:45:16
disqus: y
---

## 题意：
给一个start和一个end,看能否经过单词在dict中的变换

## 要求：


## 思路：
bfs
python做法：
http://chaoren.is-programmer.com/posts/43039.html

## 更新：
总结leetcode搜索题目

## 代码：

### C++:

{% highlight c++ %}
class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        if(start.length()!=end.length())
            return 0;
        queue<string>q;
        q.push(start);
        dict.erase(start);
        int ans=1;
        int cnt=1;
        while(dict.size()>0 && !q.empty())
        {
            string cur=q.front();
            q.pop();
            cnt--;
            for(int i=0;i<cur.length();i++)
            {
                string temp=cur;
                for(char j='a';j<='z';j++)
                {
                    if(temp[i]==j)
                        continue;
                    temp[i]=j;
                    if(temp==end)
                        return ans+1;
                    if(dict.find(temp)!=dict.end())
                        q.push(temp);
                    dict.erase(temp);
                }
            }
            if(cnt==0)
            {
                cnt=q.size();
                ans++;
            }
        }
        return 0;
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        wordLen = len(start)
        queue = collections.deque([(start, 1)])
        while queue:
            curr = queue.popleft()
            currWord = curr[0]; currLen = curr[1]
            if currWord == end: return currLen
            for i in xrange(wordLen):
                part1 = currWord[:i]; part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in dict:
                            queue.append((nextWord, currLen + 1))
                            dict.remove(nextWord)
        return 0
 {% endhighlight %}
