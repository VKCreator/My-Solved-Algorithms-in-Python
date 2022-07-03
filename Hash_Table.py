# check duplicate
voted = {}


def check_voter(name):
    if voted.get(name):
        print('Kick them out!')
    else:
        voted[name] = True
        print('Let them vote!')


check_voter('tom')
check_voter('john')
check_voter('john') # duplicate


# cache

cache = {}


def get_data_from_server(url):
    return f'content {url}'


def get_page(url):
    if cache.get(url):
        print('cache')
        return cache[url]
    else:
        print('no cache')
        data = get_data_from_server(url)
        cache[url] = data
        return data


content_google = get_page('google.com')
print(content_google)
print(get_page('google.com'))


# collision
# если несколько ключей отображаются на один элемент, в этом элементе
# создается связанный список

class HashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value


t = HashTable()
# collision
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))

t['march 6'] = 3
print(t['march 6'])


class HashTableCollision:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                break
        else:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                break


t = HashTableCollision()

t['march 6'] = 3
t['march 17'] = 8
t['march 6'] = 78
print(t['march 6'])
print(t['march 17'])

del t['march 17']
print(t['march 17'])