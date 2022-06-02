#!/usr/bin/pytthon3
if __name__ == "__main__":
    from hidden_4 import*
    nam == dir()
    for i in range(0, len(nam)):
        if nam[i][0:2] != "__":
            print("{}".format(nam[i]))
