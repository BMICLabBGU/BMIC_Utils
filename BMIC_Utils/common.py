

def autoArgs(args:dict,c_obj:object):
    """
    The function takes a dictionary of arguments and an object, and returns a new instance of
    the object with the specified arguments.
    
    :param args: A dictionary containing the arguments to be passed to the object's constructor
    :type args: dict
    :param c_obj: An object that you want to create using the provided
                    arguments
    :type c_obj: object
    :return: an instance of the class `c_obj` with the arguments specified in the `args` dictionary.
    """
    func_args_keys = list(c_obj.__init__.__code__.co_varnames)[1:]
    args_keys = list(set(func_args_keys).intersection(args.keys()))
    
    return c_obj(**{x:args[x] for x in args_keys})
