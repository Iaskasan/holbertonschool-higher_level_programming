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
        return iter(self.count)
