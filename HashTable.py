from LinkedList import *



# Chained hash table used in case a need for a larger amount of deliveries.
class ChainedHashtable:
    """ Chained Hashtable

        A linked list of Keys and Values are stored in the links array, which holds a linked list of all the mapped values
    """
    #  Use to change size of HashTable
    Size = 10

    #  Method to add a new key value pair to ChainedHashTable entity
    def put(self, key, value):
        link_list = self.links[self.hash(key)]
        if link_list is None:  # If current hash bucket is empty, adds key value pair and sets the head to new node
            node = Link(key=key, value=value)
            link_list = LinkedList(head=node)
            self.links[self.hash(key)] = link_list
            return
        cur_node = link_list.head
        while cur_node is not None:  # Updates Key Value pair if a key is found.
            if cur_node.key == key:
                cur_node.value = value
                return
            else:
                cur_node = cur_node.next
        link_list.push(Link(key=key, value=value))

    #  Simple hash function, takes in a key and returns key modulo the size of the table.
    def DivisionHash(self, key, size):  # Size variable at beginning of ChainedHashTable class for easy modification.
        return key % size

    def get(self, key):
        link_list = self.links[self.hash(key)]
        if link_list is None:
            return None
        cur_node = link_list.head
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return None


    # Space-time complexity is O(N)
    # Takes in a key(package number) and value(package number + all data) and updates key, value pair.
    def update(self, key, value):
        link_list = self.links[self.hash(key)]
        if link_list is None:
            return None
        cur_node = link_list.head
        while cur_node is not None:
            if cur_node.key == key:
                cur_node.value = value

                return None
            else:
                cur_node = cur_node.next
        else:
            print('There was an error with updating on key: ' + key)


    def search(self, key):
        link_list = self.links[self.hash(key)]
        if link_list is None:
            return str(self.hash(key))
        search_result = ""
        cur_node = link_list.head
        search_result += str(self.hash(key)) + " "
        while cur_node is not None:
            search_result += str(cur_node.value) + " "
            if cur_node.key == key:
                return search_result
            else:
                cur_node = cur_node.next
        return search_result

    def insert(self, key, value):
        self.put(key, value)

    def hash(self, key):
        return self.DivisionHash(key, ChainedHashtable.Size)

    def __str__(self):
        lines = []
        for i in range(len(self.links)):
            if self.links[i] == None:
                lines.append("" + str(i) + "\t")
            else:
                lines.append("" + str(i) + "\t" + str(self.links[i]))
        return "\n".join(lines)

    def __init__(self):
        self.links = [None] * ChainedHashtable.Size
