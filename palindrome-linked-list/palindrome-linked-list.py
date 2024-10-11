# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        is_palindromic = True
        while current != None:
            stack.append(current.val)
            current = current.next
        
        while head != None:
            value = stack.pop()
            
            if head.val == value:
                is_palindromic = True
            else:
                is_palindromic = False
                break
            
            head = head.next
            
        return is_palindromic