class Solution(object):
    def hasCycle(self, head):
        current = last = head
        while current and current.next:
            current = current.next.next
            last = last.next
            if last == current:
                return True
        return False