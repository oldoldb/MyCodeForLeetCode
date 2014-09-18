---
layout: post
title: Word Ladder II 
date: 2014-09-018 16:57:16
disqus: y
---

## 题意：
给定起点单词和终点单词，以及词典，求从起点单词转换成终点单词的所有路径（每次只能变换一个字母，且变换后的单词仍在词典中）

## 要求：


## 思路：
When searching in BFS, maintain parent pointer of each node discovered in current level back to parent node in previous level, and finally use DFS to find all path from end to start.

## 更新：
总结leetcode树的题目

## 代码：

### Java:

{% highlight java %}
public class Solution {
    public List<List<String> > findLadders(String start, String end, HashSet<String> dict){
    HashMap<String, Queue<String> > adjMap = new HashMap<String, Queue<String> >();
    int curlen = 0;
    boolean isfound = false;
    List<List<String> >  res = new ArrayList<List<String> >();
    Queue<String> queue = new LinkedList<String>();
    Set<String> unvisited = new HashSet<String>(dict);
    Set<String> visitedthislev = new HashSet<String>();
    unvisited.add(end);
    queue.offer(start);
    int curlev = 1;
    int nextlev = 0;
    for(String word : unvisited){
        adjMap.put(word, new LinkedList<String>());
    }
    unvisited.remove(start);

    while(!queue.isEmpty()){
        String curladder = queue.poll();
        for(String nextladder : getNextLadder(curladder, unvisited)){
            if(visitedthislev.add(nextladder)){
                nextlev++;
                queue.offer(nextladder);
            }
            adjMap.get(nextladder).offer(curladder);
            if(nextladder.equals(end) && !isfound){
                isfound = true;
                curlen+= 2;
            }
        }
        if(--curlev == 0){
            if(isfound){
                break;
            }
            unvisited.removeAll(visitedthislev);
            curlev = nextlev;
            nextlev = 0;
            curlen ++;
        }
    }
    if(isfound){
        LinkedList<String> temp = new LinkedList<String>();
        temp.addFirst(end);
        getLadders(start, end, temp, res, adjMap, curlen);
    }
    return res;
}

    private List<String> getNextLadder(String curladder, Set<String> unvisited){
        List<String> nextladders = new ArrayList<String>();
        StringBuffer replace = new StringBuffer(curladder);
        for(int i=0;i<curladder.length();i++){
            char old = replace.charAt(i);
            for(char ch='a';ch<='z';ch++){
                replace.setCharAt(i, ch);
                String replaced = replace.toString();
                if(ch!=curladder.charAt(i) && unvisited.contains(replaced)){
                    nextladders.add(replaced);
                }
            }
            replace.setCharAt(i, old);
        }
        return nextladders;
    }
    private void getLadders(String start, String curladder, LinkedList<String> temp, List<List<String> > ans, HashMap<String, Queue<String> > adjMap, int len){
        if(curladder.equals(start)){
            ans.add(new ArrayList<String>(temp));
        }else if(len>0){
            Queue<String> adjs = adjMap.get(curladder);
            for(String lad : adjs){
                temp.addFirst(lad);
                getLadders(start, lad, temp, ans, adjMap, len-1);
                temp.removeFirst();
            }
        }
    }
}
 {% endhighlight %}

