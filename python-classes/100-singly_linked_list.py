#!/usr/bin/python3


class Node:
    '''Class Node that defines a node of a singly linked list'''
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''This class defines a singly linked list'''
    def __init__(self):
        self.list = []

    def sorted_insert(self, value):
        self.list.append(value)
        self.list = sorted(self.list)

    def __str__(self) -> str:
        str_print = ""
        lenght = len(self.list)
        for i in range(lenght):
            if i == lenght - 1:
                str_print = f"{str_print}{self.list[i]}"
            else:
                str_print = f"{str_print}{self.list[i]}\n"
        return str_print
