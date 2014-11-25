---
layout: post
title: Populating Next Right Pointers in Each Node II
date: 2014-08-18 18:56:16
disqus: y
---

## 题意：
按要求重构二叉树

## 要求：


## 思路：
与Populating Next Right Pointers in Each Node不同之处在于本题的二叉树可以是任意形式的。
因此，对一个节点需要向右找到第一个节点。
对于left，如果right不存在，就在father的next节点去找left/right，依次找下去。
对于right，直接在father的next节点开始找。

需要注意的是，要先处理右子树，再处理左子树。

## 代码：

## 更新：
总结leetcode树的题目

### C++:

{% highlight c++ %}
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        while(root)
        {
            TreeLinkNode *phead=NULL;
            TreeLinkNode *prev=NULL;
            while(root)
            {
                if(root->left)
                {
                    if(prev)
                        prev->next=root->left;
                    else
                        phead=root->left;
                    prev=root->left;
                }
                if(root->right)
                {
                    if(prev)
                        prev->next=root->right;
                    else
                        phead=root->right;
                    prev=root->right;
                }
                root=root->next;
            }
            root=phead;
        }
    }
};


 {% endhighlight %}
### python:

{% highlight python %}

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root==None:
            return
        if root.left!=None:
            root.left.next = root.right
            if root.right==None:
                node = root.next
                while node!=None and root.left.next==None:
                    root.left.next = node.left
                    if node.left==None:
                        root.left.next = node.right
                    node = node.next
        if root.right!=None:
            node = root.next
            while node!=None and root.right.next==None:
                root.right.next = node.left
                if node.left==None:
                    root.right.next = node.right
                node = node.next
        self.connect(root.right)
        self.connect(root.left)
 {% endhighlight %}
