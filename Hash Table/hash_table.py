class HashTable:
    
    collection = {}

    def hash(self, string):
        hash_value = 0
        for i in string:
            hash_value += ord(i)
        return hash_value

    def add(self, key, value):
        hashed_key = hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}
    
    def remove(self, key):
        hashed_value = hash(key)
        if hashed_value in self.collection:
            if len(self.collection[hashed_value] == 1):
                del self.collection[hashed_value]
            else:
                del self.collection[hashed_value][key]
        else:
            pass