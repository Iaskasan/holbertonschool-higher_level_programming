#!/usr/bin/python3


class SwimMixin:
    ''' class SwimMixin'''
    def swim(self):
        print("The creature swims!")

    def fly(self):
        print("The creature flies!")


class FlyMixin:
    ''' class FlyMixin'''
    def swim(self):
        print("The creature swims!")

    def fly(self):
        print("The creature flies!")


class Dragon(FlyMixin, SwimMixin):
    '''
    Sibling class Dragon that inehrits
    both from FlyMixin and SwimMiwin
    '''
    def roar(self):
        print("Roooooaaarrr!")
