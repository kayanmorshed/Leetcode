# definition of a double linked list
class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # create two sentinels and initialize the pointers
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove the given 'node' from the linked list
    def remove_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    # insert the given 'node' to the right side of the linked list
    def insert_node(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key]) # remove from the linked list
            self.insert_node(self.cache[key]) # insert the removed node to the right
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if hit, remove the node from the list
        if key in self.cache:
            self.remove_node(self.cache[key])
        
        # update the mapping with the updated/added key-value pair
        self.cache[key] = ListNode(key, value)
        
        # insert the updated node into the list
        self.insert_node(self.cache[key])
        
        # check whether the cache is full; if yes, remove the LRU node
        if len(self.cache) > self.cap:
            lru_node = self.left.next
            self.remove_node(lru_node) # remove from the list
            del self.cache[lru_node.key] # remove the mapping of the lru node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)