'''
Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head
        while fast.next and slow:
            fast , slow = fast.next.next, slow.next
        return slow

class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:     
        temp = head  
        count = 0        
        while head: 
            # only update when count is odd 
            if (count & 1):  
                temp = temp.next
            head = head.next
            # increment count in each iteration  
            count += 1 
        return temp

class Solution3:
    def middleNode(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast else slow



