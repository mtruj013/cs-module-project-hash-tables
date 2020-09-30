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
        self.capacity = capacity
        self.buckets = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        list_length = len(self.buckets)

        return list_length

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # load factor = number of items / table size

        # items_num = hash(self)

        # return items_num % len(table)
        pass


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # 64 bit FNV_prime = 240 + 28 + 0xb3 = 1099511628211
        FNV_prime = 1099511628211

        # 64 bit offset_basis = 14695981039346656037
        offset_basis = 14695981039346656037

        # hash = offset_basis
        # for each octet_of_data to be hashed
        #  hash = hash * FNV_prime
        #  hash = hash xor octet_of_data
        # return hash
        hash = offset_basis
        key = str(key).encode()    

        for i in key:
            hash = hash * FNV_prime
            hash = hash ^ i
            
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # node = HashTableEntry(key, value)

        # Find the index
        index = self.hash_index(key)
        # Search the list at that index for the key
        current = self.buckets[index]
        # self.buckets[index] = node

        # print(self.buckets[index])
        while current != None and current.key != key:
            current = current.next
        # If found, update the value
        if current != None:
            current.value = value
        # If not found, make a new entry and insert it at the head of the list.]
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.buckets[index]
            self.buckets[index] = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # get the index for the key
      
        # search the linked list for the key at that index
            # if found, delete it, return it
        # else return None

        
        # while head:
        #     if head.key == key:
        #         prev.next = cur.next
        #         cur.next = None
        #         return cur
        #     prev = prev.next
        #     cur = cur.next
        # return None

    # get the index for the key
    # search the linked list for the key at that index
    # if found, delete it, return it
    # else return None

        index = self.hash_index(key)
        head = self.buckets[index]
        prev = None

        # if theres nothing

        while head is not None and head.key != key:
            prev = head
            head = prev.next
        
        if head is None:
            return None
        else:
            if prev is None:
                self.buckets[index] = head.next
            else:
                prev.next = head.next
                

        # if there's only 1 thing
        # if head.key == key:
        #     old_head = head
        #     head = head.next
        #     old_head.next = None
        #     return old_head
        
        # # general case
        # prev = head
        # cur = head.next

        # while cur:
        #     if cur.key == key:
        #         prev.next = cur.next
        #         cur.next = None
        #         return cur

        #     prev = prev.next
        #     cur = cur.next
        # return None 


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # get the index for the key
        index = self.hash_index(key)
        # search the linked list at that index for the key
        current = self.buckets[index]
        while current:
            # if found, return the value
            if current.key == key:
                return current.value
            current = current.next
        return current


        # index = self.hash_index(key)
        # if self.buckets[index]:
        #     return self.buckets[index].value
        # else:
        #     return None



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
