# define a class ListNode to create a doubly linked list
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        
        # define the pointers
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # add sentinels
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # insert node at right
    def insert_node(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    # insert a node from the linked list
    def remove_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key is hit, remove that node        
        if key in self.cache:
            self.remove_node(self.cache[key])
        
        # update the pointer in the hashmap
        self.cache[key] =  ListNode(key, value)
        
        # insert the node in the linked list
        self.insert_node(self.cache[key])
        
        # when the cache is full, remove the LRU
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove_node(lru) # remove the LRU node from the linked_list
            del self.cache[lru.key] # remove the mapping of the deleted node from the hashmap 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)