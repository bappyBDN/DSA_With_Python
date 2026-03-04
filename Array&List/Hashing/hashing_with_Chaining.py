"""Hashing with Chaining Implementation
Last Updated : 1 Aug, 2025
In hashing there is a hash function that maps keys to some values. But these hashing functions may lead to a collision that is two or more keys are mapped to same value. Chain hashing avoids collision. The idea is to make each cell of hash table point to a linked list of records that have same hash function value.

For a more detailed explanation and theoretical background on this approach, please refer to Hashing | Set 2 (Separate Chaining).

Let's create a hash function, such that our hash table has 'n' number of buckets. 

To insert a node into the hash table, we first compute the hash index for the given key using a hash function:
hashIndex = key % noOfBuckets.
This index determines the appropriate bucket where the node should be inserted.

Example:
noOfBuckets = 7
keys to insert = [15, 11, 27, 8]

For each key:

15 % 7 = 1
11 % 7 = 4
27 % 7 = 6
8 % 7 = 1"""
class Hash:
    def __init__(self, NoofBuckets):
        self.NoofBuckets=NoofBuckets
        self.hashTable=[None]*self.NoofBuckets
    def insert(self,key):
        index=key%self.NoofBuckets
        if self.hashTable[index] is None:
            self.hashTable[index]=[key]
        else:
            self.hashTable[index].append(key)
    def remove(self,key):
        index=key%self.NoofBuckets
        if self.hashTable[index] is not None:
            try:
                self.hashTable[index].remove(key)
            except ValueError:
                print(f"Key {key} not found in the hash table.")
    def search(self,key):
        index=key%self.NoofBuckets
        if self.hashTable[index] is not None:
            return key in self.hashTable[index]
        return False
            
        
    def display(self):
        for i in range(self.NoofBuckets):
            print(f"Bucket {i}:", end=" ")
            if self.hashTable[i] is not None:
                print(" -> ".join(map(str, self.hashTable[i])))
            else:
                print("None")
if __name__ == "__main__":
    NoofBuckets=7
    hashTable=Hash(NoofBuckets)
    keys=[15, 11, 27, 8]
    for key in keys:
        hashTable.insert(key)
    print("Hash Table with Chaining:")
    hashTable.display()
    hashTable.remove(11)
    print("\nHash Table after removing key 11:")
    hashTable.display()
    search_key=27
    print(f"\nSearching for key {search_key}: {'Found' if hashTable.search(search_key) else 'Not Found'}")

