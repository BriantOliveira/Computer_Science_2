

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

def _get_hash(self,key):
    hash = 0
    for char in str(key):
        hash += ord(char)
    return hash % self.size

    """ function check if key value is = to none if not add 1 """
def _add_hash_(self,key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    if self.map[key_hash] is None:
        self.map[key_hash] = list([key_value])
        return True
    else:
        for pair in self.map[key_hash]:
            if pair[0] == key():
                pair[1] = value
                return True
        self.map[key_hash].append([key_value])
    """ get the hash given the key and locate the cell and if cell is != none then loop and find/return value of the key"""
def _get_hash_(self,key):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]
    """function that will locate the key and check if the cell is none means that is does not exist"""
    def _delete_hash_():
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def _display_hash_(self):
        print("---PHONEBOOK---")
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()

h.add('Elliot', '978-677')
h.add('Rohan', '774-312')
h.add('Willie', '999-111')
h.add('Alan', '678-234')
h.add('Tassos', '911-569')
h.add('Tia', '415-332')

h.display()

h.delete('Elliot')

h.display()

print('Rohan:' + h.get('Rohan'))
