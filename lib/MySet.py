class MySet:

    def __init__(self, enumerable = []) -> None:
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        elements = ','.join(str(value) for value in self.dictionary.keys())
        return f'MySet: {{{elements}}}'