class Link:

    #  Link is a key, value pair used in a linked list.
    #  Link is used in ChainedHashTable

    def __str__(self):
        if self.next == None:
            return str(self.value) + " "
        else:
            return str(self.value) + " " + str(self.next)

    def __init__(self, key=0, value=0, next=None):
        self.key = key
        self.value = value
        self.next = next


class LinkedList:

    def push(self, new, prev=None):
        if prev is None:
            new.next = self.head
            self.head = new
        else:
            new.next = prev.next
            prev.next = new

    def pop(self, index=0):
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1

        if prev_node is None:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            prev_node = cur_node.next
            return cur_node

    def insert(self, node, index=0):
        if node is None:
            raise Exception("node is None Type")
            return
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1

        if prev_node is None:
            self.head = node
        else:
            prev_node.next = node

        node.next = cur_node

    def __str__(self):
        if self.head is None:
            return ""
        else:
            return str(self.head)

    def __init__(self, head=None):
        self.head = head

