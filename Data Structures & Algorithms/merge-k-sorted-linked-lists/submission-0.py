# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def mergeTwoLists(firstHead, secondHead):
            dummy = node = ListNode()

            while firstHead and secondHead:
                if firstHead.val < secondHead.val:
                    node.next = firstHead
                    firstHead = firstHead.next
                else:
                    node.next = secondHead
                    secondHead = secondHead.next
                node = node.next
            
            node.next = firstHead or secondHead
            return dummy.next
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i-1], lists[i])
        
        return lists[-1]

