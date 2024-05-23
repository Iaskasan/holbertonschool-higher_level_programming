#!/usr/bin/python3
'''Module for the class CountedIterator'''


class CountedIterator:
    def __init__(self, obj):
        self.obj = obj
        self.iter = iter(obj)
        self.count = 0

    def __next__(self):
        self.count += 1
        if self.count > len(self.obj):
            raise StopIteration
        return next(self.iter)
    
    def get_count(self):
        return self.count

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")