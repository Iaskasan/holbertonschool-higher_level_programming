#!/usr/bin/python3
'''Class VerboseList that will extend/modify the class list'''


class VerboseList(list):
    '''This class rewrite some methods of the in-built class list'''
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
