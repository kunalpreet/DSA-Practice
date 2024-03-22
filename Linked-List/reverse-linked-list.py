class ListNode:
	def __int__(self, val=0, next=None):
		self.val = val
		self.next = next

	def reverseList(self, head):
		prev, curr = None, head

		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		return prev
