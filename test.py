from itertools import zip_longest

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

    def __init__(self, *args, attributes=None, values=None, pair_flag=True):
        num_attributes_added      = 0
        num_attributes_not_added  = 0
        attributes_not_added_list = []

        if len(args) == 1 and type(args[0]) is dict and attributes is None and values is None:
            self.__dict__ = args[0]
            num_attributes_added = len(args[0])

        elif len(args) == 1 and type(args[0]) is dict:
            for k, v in args[0].items():
                self.__dict__[k] = v
                num_attributes_added += 1


        if attributes is not None and values is not None and is_iterable(attributes) and is_iterable(values):
            zipped = zip_longest(attributes, values, fillvalue=None)

            for attribute, value in zipped:
                if is_hashable(attribute):
                    self.__dict__[attribute] = value
                    num_attributes_added += 1

                else:
                    num_attributes_not_added += 1
                    attributes_not_added_list.append({'attribute': attribute, 'value': value})
                    continue

        elif attributes is None and values is None and not num_items_is_even(len(args)):
            for arg in args:
                if is_hashable(arg):
                    self.__dict__[arg] = None
                    num_attributes_added += 1

                elif not is_hashable(arg) and is_iterable(arg):
                    for item in arg:
                        if is_hashable(item):
                            self.__dict__[item] = None
                            num_attributes_added += 1

                else:
                    num_attributes_not_added += 1
                    attributes_not_added_list.append({'attribute': arg, 'value': None})
                    continue

        elif attributes is None and values is None and num_items_is_even(len(args)) and pair_flag:
            for i in range(0, len(args), 2):
                if is_hashable(args[i]):
                    try:
                        self.__dict__[args[i]] = args[i+1]
                        num_attributes_added += 1

                    except IndexError:
                        num_attributes_not_added += 1
                        attributes_not_added_list.append({'attribute': args[i], 'value': None})
                        continue

                elif not is_hashable(args[i]) and is_iterable(args[i]):
                    for item in args[i]:
                        if is_hashable(item):
                            try:
                                self.__dict__[item] = args[i+1]
                                num_attributes_added += 1

                            except IndexError:
                                num_attributes_not_added += 1
                                attributes_not_added_list.append({'attribute': args[i], 'value': None})
                                continue

                        else:
                            num_attributes_not_added += 1
                            attributes_not_added_list.append({'attribute': arg, 'value': None})
                            continue

                else:
                    num_attributes_not_added += 1
                    attributes_not_added_list.append({'attribute': arg, 'value': None})
                    continue

        if num_attributes_not_added: #if num_attributes_not_added > 0
            print("Successfully added {0} attribute(s)!  The following {1} attribute(s) could not be added:\n{2}".format(num_attributes_added, num_attributes_not_added, attributes_not_added_list))
        else:
            print("{} attribute(s) added successfully!".format(num_attributes_added))


def main():

    a = Name("Bob")
    print(a.__dict__)

    b = Name("Bob", "cat")
    print(b.__dict__)

    c = Name(['type', 'null', 'category', 'I don\'t know'])
    print(c.__dict__)

    d = Name({'one':1, 'two': 2}) # this test currently passing, but printing incorrect number of attributes added (a/o 4/26/2020)
    print(d.__dict__)

    e = Name([1,2,3],'apple', "monkey", ('see', 'do'))
    print(e.__dict__)

    f = Name(attributes=['ten', 'nine', 'eight'], values=['10', '9'])
    print(f.__dict__)

    tuple1 = ("this is an attribute", "Truthy", 1, 0.01, 'Falseyy')
    list_1 = ["yay", "fAlSe", 0, 0.99, 'TrUe', 'more values than attributes', 'uh-oh, there\'s more values, but no more attributes']
    dict_1 = {'attribute1': 1.0, 'attribute2': [2, 2.0], 'attribute3': "3"}

    complex_example = Name(dict_1, attributes=(tuple1), values=list_1)
    print(complex_example.__dict__)

    print(complex_example.attribute2)

if __name__ == '__main__':
    main()
