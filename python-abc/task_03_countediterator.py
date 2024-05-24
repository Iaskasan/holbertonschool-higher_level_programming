#!/usr/bin/python3
'''Module for the class CountedIterator'''


class CountedIterator:
    def __init__(self, obj):
        self.obj = obj
        self.iter = 0
        self.count = 0

    def __next__(self):
        if self.iter > len(self.obj):
            raise StopIteration
        self.iter += 1
        self.count += 1
        return self.obj[self.iter]

    def get_count(self):
        return self.count

    def __iter__(self):
        return self


if __name__ == "__main__":

    data = None
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
