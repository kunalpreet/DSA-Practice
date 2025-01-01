class ListNode:
	def __int__(self, val=0, next=None):
		self.val = val
		self.next = next

	def reverseList(self, head):
		prev, curr = None, head
		# curr: 1 -> 2 -> 3 -> None
		# prev:
		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		return prev
