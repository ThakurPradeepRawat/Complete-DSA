"""25 . Reverse Nodes in k-Group"""
"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        current = head 
        count  = 0 
        while(count<k):
            if(current==None):
                return head 
            current = current.next 
            count+=1
        prev = self.reverseKGroup(current, k)
        temp = head 
        count = 0 
        while(count<k):
            next_temp = temp.next 
            temp.next = prev 
            prev = temp 
            temp= next_temp
            count+=1
        return prev
        
        
        
        