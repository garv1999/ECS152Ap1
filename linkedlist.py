# code from https://realpython.com/linked-lists-python/
# adapted into doubly linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

	def __repr__(self):
		return self.data

class LinkedList:
	def __init__(self, nodes=None):
		self.head = None
		self.tail = None
		if nodes is not None:
			hnode = Node(data=nodes.pop(0))
			tnode = Node(data=nodes.pop())
			self.head = hnode
			self.tail = tnode if nodes.len() is 0 else hnode
			for elem in nodes:
				node.next = Node(data=elem)
				if (node.next is not None):
					node.next.prev = node
				node = node.next

	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		return " -> ".join(nodes)

	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def add_first(self, node):
		if not self.head:
			self.head = node
			self.tail = node
			return

		self.head.prev = node
		node.next = self.head
		node.prev = None
		self.head = node

	def add_last(self, node):
		if not self.head:
			self.head = node
			self.tail = node
			return

		node.prev = self.tail
		node.prev.next = node
		self.tail = node

	def add_after(self, target_node_data, new_node):
		if not self.head:
			raise Exception("List is empty")

		if self.tail.data == target_node_data:
			return self.add_last(new_node)

		for node in self:
			if node.data == target_node_data:
				new_node.next = node.next
				new_node.prev = node
				node.next = new_node
				return

		raise Exception("Node with data '%s' not found" % target_node_data)

	def add_before(self, target_node_data, new_node):
		if not self.head:
			raise Exception("List is empty")

		if self.head.data == target_node_data:
			return self.add_first(new_node)

		prev_node = self.head
		for node in self:
			if node.data == target_node_data:
				prev_node.next = new_node
				new_node.prev = prev_node
				new_node.next = node
				node.prev = new_node
				return
			prev_node = node

		raise Exception("Node with data '%s' not found" % target_node_data)

	def is_empty(self):
		return self.head is None

	def remove_node(self, target_node_data):
		if not self.head:
			raise Exception("List is empty")

		if self.head.data == target_node_data:
			self.head = self.head.next
			return

		if self.tail.data == target_node_data:
			self.tail = self.tail.prev
			return

		previous_node = self.head
		for node in self:
			if node.data == target_node_data:
				previous_node.next = node.next
				node.next.prev = previous_node
				return
			previous_node = node

		raise Exception("Node with data '%s' not found" % target_node_data)
