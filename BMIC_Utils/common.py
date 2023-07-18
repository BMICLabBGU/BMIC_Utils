

def autoArgs(args,c_obj:object):
    func_args_keys = list(c_obj.__init__.__code__.co_varnames)[1:]
    args_keys = list(set(func_args_keys).intersection(args.keys()))
    
    return c_obj(**{x:args[x] for x in args_keys})
