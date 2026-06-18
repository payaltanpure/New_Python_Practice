class demo:
    #default constructor
    def __init__(self):
        print("default con called")

    def __init__(self, name, bases, dict, /, **kwds):
        pass


obj= demo()