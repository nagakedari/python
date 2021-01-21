class HashTable:

    def __init__(self):
        self.a = [None] * 25
    
    def calculate_hash_value(self, key):
        hash_code = ord(key[0]) * 100 + ord (key[1])
        print(hash_code)
        index = hash_code % 10
        print('index: {}'.format(index))
        return index
    
    def store(self, key, value):
        index = self.calculate_hash_value(key)
        if self.a[index]:
            self.a[index].append({key: key, value: value})
        else:
            self.a[index] = []
    
    def lookup(self, key):
        index = self.calculate_hash_value(key)
        if self.a[index]:
            for obj in self.a[index]:
                if key == obj.key:
                    return obj.value
        return -1


hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('key1'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('key1'))

# Test store
hash_table.store('key1', 'UDACITY')
# Should be 8568
print(hash_table.lookup('key1'))

# Test store edge case
hash_table.store('key2', 'UDACIOUS')
# Should be 8568
print(hash_table.lookup('key2'))