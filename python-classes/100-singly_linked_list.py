#!/usr/bin/python3
'''Defines a a node of a singled linked list'''


class Node:
    '''Class Node that defines a node of a singly linked list'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''returns the data, must be an int'''
        return self.__data

    @data.setter
    def data(self, value):
        '''checks if the data is an int, otherwise raise a Typerror'''
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        '''return a node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        checks if the next_node has the right class (Node) or is None
        and gives it to the constructor
        '''
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''This class defines a singly linked list'''
    def __init__(self):
        '''Basic constructor that initialises an empty list'''
        self.list = []

    def sorted_insert(self, value):
        '''
        takes a value as input and adds it to a list
        before sorting the list
        '''
        self.list.append(value)
        self.list = sorted(self.list)

    def __str__(self) -> str:
        '''the __str__ method that returns each elements of
        the list followed by a new line
        output = str
        '''
        str_print = ""
        lenght = len(self.list)
        for i in range(lenght):
            if i == lenght - 1:
                str_print = f"{str_print}{self.list[i]}"
            else:
                str_print = f"{str_print}{self.list[i]}\n"
        return str_print
