# Given a linked list, check if there's a cycle

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
        return False
    else:
        curr = head
        fast_curr = head
        while curr != None and fast_curr != None:
            if curr.next:
                curr = curr.next
            else:
                return False
            if fast_curr.next and fast_curr.next.next:
                fast_curr = fast_curr.next.next
            else:
                return False
            
            if curr.val == fast_curr.val:
                return True
    
    return False

# Tests
head = ListNode(0)
curr = head
for i in range(10):
    curr.next = ListNode(i)
    curr = curr.next

head2 = ListNode(0)
head2.next = ListNode(1)
curr = head2.next
curr.next = head2

print(hasCycle(head))
print(hasCycle(head2))
