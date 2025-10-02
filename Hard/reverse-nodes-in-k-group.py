# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are k nodes left
            kth = prev_group
            count = 0
            while count < k and kth.next:
                kth = kth.next
                count += 1
            if count < k:
                break
            
            # Reverse k nodes
            group_prev = prev_group.next
            curr = group_prev.next
            for _ in range(k - 1):
                temp = curr.next
                curr.next = prev_group.next
                prev_group.next = curr
                curr = temp
            group_prev.next = curr
            prev_group = group_prev
        
        return dummy.next
