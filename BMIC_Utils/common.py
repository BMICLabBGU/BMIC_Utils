import nibabel as nib
import numpy as np
import yaml
from easydict import EasyDict


def autoArgs(args,c_obj:object):
    func_args_keys = list(c_obj.__init__.__code__.co_varnames)[1:]
    args_keys = list(set(func_args_keys).intersection(args.keys()))
    
    return c_obj(**{x:args[x] for x in args_keys})

def yaml2Obj(yml_path:str):
    with open(yml_path,'r') as fd:
        yml_obj = EasyDict(yaml.safe_load(fd))
        
    return yml_obj