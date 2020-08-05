class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Print entire linked list."""

        if self.head is None:
            return "[Empty List]"

        cur = self.head
        s = ""

        while cur != None:
            s += f'({cur.value})'

            if cur.next is not None:
                s += '-->'

            cur = cur.next

        return s

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur

            cur = cur.next

        return None

    def delete(self, key):
        cur = self.head

        # Special case of deleting head

        if cur.key == key:
            self.head = cur.next
            return cur

        # General case of deleting internal node

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # If we got here, nothing found

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_or_overwrite_value(self, key, value):
        node = self.find(key)

        if node is None:
            # Make a new node
            self.insert_at_head(HashTableEntry(key, value))

        else:
            # Overwrite old value
            node.value = value






class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = [None] * MIN_CAPACITY
        self.stored = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here



    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.stored / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        l = self.capacity[self.hash_index(key)]
        self.stored += 1
        if l == None:
            l = LinkedList()
            l.insert_or_overwrite_value(key, value)
            self.capacity[self.hash_index(key)] = l
            return

        else:
            l.insert_or_overwrite_value(key, value)
            return



    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if self.capacity[index]:
            self.stored -= 1
            self.capacity[index].delete(key)
        else:
            print("no key found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        found = self.capacity[index].find(key)
        if found:
            return found.value
        else:
            return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
