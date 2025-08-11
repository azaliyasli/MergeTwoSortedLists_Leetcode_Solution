# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        lastNode = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                lastNode.next = list1
                list1 = list1.next
            else:
                lastNode.next = list2
                list2 = list2.next
            lastNode = lastNode.next #Save the lastNode

        lastNode.next = list1 if list1 else list2 #For the remainders if the lists are not in equal length
        return mergedList.next
