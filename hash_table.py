

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

def _get_hash(self,key):

    """ function check if key value is = to none if not add 1 """
def add(self,key, value):
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
def get(self,key):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]

    def delete():


    def print(self):

h = HashMap()
h.add('Elliot', '978-677')
h.add('Rohan', '774-312')
h.add('Willie', '999-111')
h.add('Alan', '678-234')
h.add('Tassos', '911-569')
h.add('Tia', '415-332')
