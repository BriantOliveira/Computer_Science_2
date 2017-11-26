

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self,key):

    def add(self,key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pain in self.map[key_hash]:
                if pain[0] == key
                    pair[1] = value
                    return True
            self.map[key_hash].append[key_value]

    def get(self,key):

    def print(self):

h = HashMap()
h.add('Elliot', '978-677')
h.add('Rohan', '774-312')
h.add('Willie', '999-111')
h.add('Alan', '678-234')
h.add('Tassos', '911-569')
h.add('Tia', '415-332')
