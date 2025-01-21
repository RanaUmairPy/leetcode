class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def add(self, l1, l2):
        dummy = ListNode(0)  # Dummy node to start the result list
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.value  # Use `.value` instead of `.values`
                l1 = l1.next

            if l2:
                sum += l2.value  # Use `.value` instead of `.values`
                l2 = l2.next

            carry = sum // 10
            cur.next = ListNode(sum % 10)  # Create a new ListNode with the remainder
            cur = cur.next

        return dummy.next  # Return the next node of the dummy as the head

ob = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
ob.add(l1, l2)  # Call the method with the list of values