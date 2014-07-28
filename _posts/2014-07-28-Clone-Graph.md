---
layout: post
title: Clone Graph
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
复制一个图

## 要求：


## 思路：
1. 这题明说, label 独一无二, 那么就可以使用 hash map 存储元素

2. BFS 搜索, 边搜边向 hash map 添加元素

3. 在设置标记位上 TLE 了 N 次, 一个元素一旦被假如到 hash map, 就说明该元素已经被访问到了并已被假如到 queue 中, 同时环的问题也被克服了. 我在做的时候, 把环的问题拉出来单独处理, 但标记忘记了

4. unordered_map<node*, node*> 这种设置不是第一次见到了, 比设置成 unordered_map<int, node*> 要方便一些

5. map.count 比 map.find 要精练一些

6. 加入 map 时, 可以直接 map[] = xxx, 不用判断是否已有
## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> ans;
        if(node==NULL)
        {
            return node;
        }
        queue<UndirectedGraphNode*> q;
        q.push(node);
        while(!q.empty())
        {
            UndirectedGraphNode *s = q.front();
            q.pop();
            if(!ans.count(s))
            {
                UndirectedGraphNode *next = new UndirectedGraphNode(s->label);
                ans[s]=next;
            }
            for(int i=0;i<s->neighbors.size();i++)
            {
                UndirectedGraphNode *next = s->neighbors[i];
                if(!ans.count(next))
                {
                    UndirectedGraphNode *p = new UndirectedGraphNode(next->label);
                    ans[next]=p;
                    q.push(next);
                }
                ans[s]->neighbors.push_back(ans[next]);
            }
        }
        return ans[node];
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        dict = {}
        if node==None:
            return node
        q=[]
        q.append(node)
        while len(q)>0:
            s = q[0]
            q.pop(0)
            if s not in dict:
                next = UndirectedGraphNode(s.label)
                dict[s] = next
            for i in range(len(s.neighbors)):
                next = s.neighbors[i]
                if next not in dict:
                    p = UndirectedGraphNode(next.label)
                    dict[next]=p
                    q.append(next)
                dict[s].neighbors.append(dict[next])
        return dict[node]
 {% endhighlight %}
