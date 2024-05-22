#!/usr/bin/python3
'''This is a module for the abstract class Animal'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''This is the parent class Animal'''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''Class Dog that inherits from the class Animal'''
    def sound(self):
        return "Bark"


class Cat(Animal):
    '''Class Cat that inherits from the class Animal'''
    def sound(self):
        return "Meow"
