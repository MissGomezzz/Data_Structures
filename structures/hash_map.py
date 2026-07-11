#This is an implementation of the HasMaps, which uses a hash function that takes a key and becomes an index in an array.
# In order to manage possible collision, the chaining method is implemented

class HashMap:
    def __init__(self):
        self.array = [[] for _ in range(10)]

    def hash(self,key):
        # uses the ASCII values of each character and module with the length of the array to create the hash key
        return sum(ord(c) for c in key) % len(self.array)

    def set(self,key, value):
        index = self.hash(key)
        # Save the pair of key and value in the calculated index
        self.array[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        if not self.array[index]:
            print (f"Value at index {index} not found: empty array.")
            return None
        for item in self.array[index]:
            if item[0] == key:
                return item[1]
        print (f"EKey {key} not found.")
        return None

    def delete(self, key):
        index = self.hash(key)
        if not self.array[index]:
            print (f"Key {key} not found.")
            return None
        for item in self.array[index]:
            if item[0] == key:
                removed = item[1]
                self.array[index].remove(item)
                print (f"Element {removed} from key {key} removed.")
                return None
            print (f"Key {key} not found.")
        return None

    def print_hash_map(self):
        # Checks if all the 10 slots on the outer array is are empty
        if all(item == [] for item in self.array):
            print("Nothing to print here: hashmap empty.")
            return None
        for item in self.array:
            for pair in item:
                print (f"Key: {pair[0]}, value: {pair[1]}")
        return None

hashmap = HashMap()

hashmap.set("name", "Angela")
hashmap.set("age", 21)
hashmap.set("city", "Bogota")

print(hashmap.get("name"))
print(hashmap.get("age"))
print(hashmap.delete("name"))
print(hashmap.get("city"))
print(hashmap.get("country"))  # not found case
print(hashmap.print_hash_map())