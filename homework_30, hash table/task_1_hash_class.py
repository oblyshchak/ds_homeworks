import zlib

COEF = 0.7

class HashTable():
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        
    def calculate_coef(self):
        return self.get_len()/self.capacity
    
    def items(self):
        result = []
        for data in self.array:
            if data is not None:
                result.extend(data)
        
        return result
    
    def get_len(self):
        len_size_array = len(self.items())
        return len_size_array
        
    def create_hash(self, key):
        h = zlib.crc32(key.encode())
        return h

    def insert(self, key, value):
        index = self.create_hash(key) % self.capacity
        if self.calculate_coef() > COEF:
            raise MemoryError(self.calculate_coef())
        else:
            if self.array[index] is None:
                self.array[index] = (key, value)
            else:
                while self.array[index] is not None:
                    if index >= self.capacity:
                        index = 0
                    else:
                        index += 1
                        if self.array[index] is None:
                            self.array[index] = (key, value)
                            break
        
    def search(self, key, add = 0):
        index = self.create_hash(key) % self.capacity + add
        if index > self.capacity:
            index = 0
        k, v = self.array[index]
        if k == key:
            return k, v
        else:
            return self.search(key, add+1)
    
    def delete(self, key, add = 0):
        index = self.create_hash(key) % self.capacity + add
        if index > self.capacity:
            index = 0
        k, v = self.array[index]
        if k == key:
            del self.array[index]
        else:
            return self.delete(key, add+1)
        
    # TO DO: def visual_hash(self):
        

first = HashTable(9)
first.insert('Oleksandra', 23)
first.insert('Molita', 4)
first.insert('molita', 3)
print(first.search('molita'))
first.delete('molita')
print(first.array)

        
    
                    
                