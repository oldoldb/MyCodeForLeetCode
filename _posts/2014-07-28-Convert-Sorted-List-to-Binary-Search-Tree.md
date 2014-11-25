---
layout: post
title: Convert Sorted List to Binary Search Tree
date: 2014-07-28 15:52:16
disqus: y
---

## 题意：
将有序链表转换成二叉搜索树

## 要求：


## 思路：
Discuss里看到这个时间为O(n)，空间为O(1)的算法
采用深搜的思想，先把左子树转换完，然后根节点确定，再搜右子树
因为要改变链表，所以传参的时候用了*&,来传递对一个指针的引用

## 代码：

### C++:

{% highlight c++ %}
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *buildTree(ListNode *&head,int l,int r)
    {
        if(l>r)
        {
            return NULL;
        }
        int m=l+(r-l)/2;
        TreeNode *left=buildTree(head,l,m-1);
        TreeNode *root=new TreeNode(head->val);
        root->left=left;
        head=head->next;
        root->right=buildTree(head,m+1,r);
        return root;
    }
    TreeNode *sortedListToBST(ListNode *head) {
        int n=0;
        ListNode *temp=head;
        while(temp!=NULL)
        {
            temp=temp->next;
            n++;
        }
        return buildTree(head,0,n-1);
    }
};


 {% endhighlight %}
### python:

{% highlight python %}
‘’’
 Definition for a  binary tree node
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#
 Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
‘’’
class Solution:
    def buildTree(self,num,l,r):
        if l>r:
            return None
        m=l+(r-l)/2
        root=TreeNode(num[m])
        root.left=self.buildTree(num,l,m-1)
        root.right=self.buildTree(num,m+1,r)
        return root
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        num=[]
        temp=head
        while temp!=None:
            num.append(temp.val)
            temp=temp.next
        return self.buildTree(num,0,len(num)-1)
 {% endhighlight %}
