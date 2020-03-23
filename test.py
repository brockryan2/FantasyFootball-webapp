
class Name():

    def __init__(self, *args):
        for arg in args:
            if hasattr(arg, '__iter__'):
                if len(arg) < 1:
                    continue

                if type(arg) is dict:
                    self.__dict__ = arg

                elif type(arg) is str:
                    self.__dict__[arg] = None

                else:
                    for item in arg:
                        if hasattr(item, '__iter__') and len(item) % 2 == 0:

                            for i in range(0, len(item), 2):
                                self.__dict__[item[i]] = item[i + 1]

                        elif hasattr(item, '__iter__') and\
                            (not hasattr(item, '__hash__') or getattr(item, '__hash__') is None):

                            for i in item:
                                self.__dict__[i] = None

                        else:
                            self.__dict__[item] = None
            else:
                self.__dict__[arg] = None
