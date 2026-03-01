class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Create dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node right after head (Most Recently Used)
    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move accessed node to front
        self._remove(node)
        self._insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        # If capacity exceeded, remove LRU
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    # Utility function to display cache state
    def display(self):
        current = self.head.next
        print("Cache state (Most → Least recent): ", end="")
        while current != self.tail:
            print(f"[{current.key}:{current.value}]", end=" ")
            current = current.next
        print("\n")


# -----------------------------
# Main Driver Code
# -----------------------------
if __name__ == "__main__":

    capacity = int(input("Enter cache capacity: "))
    lru = LRUCache(capacity)

    while True:
        print("\n1. Put")
        print("2. Get")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            lru.put(key, value)
            lru.display()

        elif choice == "2":
            key = int(input("Enter key to get: "))
            result = lru.get(key)
            print("Returned:", result)
            lru.display()

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")