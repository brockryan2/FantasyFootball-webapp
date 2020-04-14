
def is_iterable(var):
    return True if hasattr(var, '__iter__') else False

def is_hashable(var):
    if hasattr(var, '__hash__') and getattr(var, '__hash__') is not None:
        return True

    else: return False

def num_items_is_even(num_args):
    return True if num_args % 2 == 0 else False

def is_empty(var):
    return True if len(var) < 1 else False

class Name():

    def __init__(self, *args, pair_flag=True):
        num_args = len(args)

        if num_items_is_even(num_args) and pair_flag:

            for i in range(0, num_args, 2):
                if is_hashable(args[i]):
                    self.__dict__[args[i]] = args[i + 1]

                else:
                    if is_iterable(args[i]):
                        for n in range(0, len(args[i])):
                            if is_hashable(args[i][n]) and is_hashable(args[i][n+1]):
                                self.__dict__[args[i][n]] = args[i][n + 1]

                            else:
                                self.__dict__[None] = args[i][n]




            #else:
                #self.__dict__[item] = None



        else:
            for arg in args:
                if is_iterable(arg) and is_empty(arg):
                    continue

                elif type(arg) is dict:
                        self.__dict__ = arg

                elif type(arg) is str:
                        self.__dict__[arg] = None

                elif len(arg) % 2 == 0:
                    for i in range(0, len(arg), 2):
                        self.__dict__[arg[i]] = arg[i + 1]

                else:
                    for item in arg:
                        if hasattr(item, '__iter__') and len(item) % 2 == 0:
                            for i in range(0, len(item), 2):
                                self.__dict__[item[i]] = item[i + 1]

                        elif is_iterable(item) and not is_hashable(item):
                            for i in item:
                                self.__dict__[i] = None

                        else:
                            self.__dict__[None] = None
                #else:
                    #self.__dict__[arg] = None


a = Name("Bob")
print(a.__dict__)

b = Name("Bob", "cat")
print(b.__dict__)

c = Name(['type', 'null', 'category', 'I don\'t know'])
print(c.__dict__)

d = Name({'one':1, 'two': 2})
print(d.__dict__)

e = Name([1,2,3],'apple', "monkey", ('see', 'do'))
print(e.__dict__)
