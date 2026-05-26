# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from collections import defaultdict
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = head
        length = 0
        while pointer:
            length +=1
            pointer = pointer.next
        
        
        pos_map = defaultdict(int)
        node_map = {}
        index_node = -1
        pointer = head
        while pointer:
            index_node +=1
            node_map[index_node] = pointer
            pointer = pointer.next
            
            if index_node%2 == 0:
                pos = int(index_node/2)
            else:
                pos = (length - int(math.ceil(index_node/2)))
            pos_map[index_node]= pos

        new_head = ListNode()
        tail = new_head
        for i in range(length):
            reorder_index = pos_map[i]
            node = node_map[reorder_index]
            tail.next = node
            tail = node
        tail.next = None
        head = new_head.next
        