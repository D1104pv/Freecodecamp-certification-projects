class HashTable:
    
    # initializing the hash table
    collection = {}

    # Method for getting basic hash value
    def hash(self, string):
        hash_value = 0
        for i in string:
            hash_value += ord(i)
        return hash_value

    # method for adding key value pairs
    def add(self, key, value):
        hashed_key = self.hash(key)
        # checking if same hash value exists
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            # making a entry
            self.collection[hashed_key] = {key: value}
    
    # method for removing values
    def remove(self, key):
        hashed_value = self.hash(key)
        # checking if key value pair exist
        if hashed_value in self.collection and key in self.collection[hashed_value]: # making sure key exist and not a duplicate hash value is stored
            del self.collection[hashed_value][key]
    
    # method for finding values
    def lookup(self, key):
        hashed_value = self.hash(key)
        if hashed_value in self.collection and key in self.collection[hashed_value]:
            return self.collection[hashed_value][key]
        else:
            return None
