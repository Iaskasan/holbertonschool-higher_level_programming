#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    try:
        for name in dir(hidden_4):
            if name[:2] != "__":
                print(name)
    except ImportError:
        pass
