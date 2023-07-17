import os
import json
import yaml
import pickle
from easydict import EasyDict

def pickle_read(file_path: str):
    """
    De-serialize an object from a provided file_path
    """

    with open(os.path.realpath(file_path), 'rb') as file:
        return pickle.load(file)


def pickle_write(obj, file_path: str):
    """
    Serialize an object to a provided file_path
    """

    file_path = os.path.realpath(file_path)
    os.makedirs(os.path.split(file_path)[0], exist_ok=True)

    with open(file_path, 'wb',) as file:
        pickle.dump(obj, file)


def json_read(path: str, easy_dict: bool = True):
    with open(os.path.realpath(path), "r") as fp:
        obj = json.load(fp)

    if easy_dict:
        obj = EasyDict(obj)

    return obj


def json_write(obj, path: str, **kwargs):
    path = os.path.realpath(path)
    os.makedirs(os.path.split(path)[0], exist_ok=True)

    if 'indent' not in kwargs:
        kwargs['indent'] = 2

    with open(path, 'w') as fp:
        json.dump(obj, fp, **kwargs)
        
def yaml_read(path: str, unsafe_load: bool = False, easy_dict: bool = True):
    with open(os.path.realpath(path), "r") as fp:
        if unsafe_load:
            obj = yaml.unsafe_load(fp)
        else:
            obj = yaml.safe_load(fp)

    if easy_dict:
        obj = EasyDict(obj)

    return obj


def yaml_write(obj, path: str):
    with open(path, 'w') as fp:
        yaml.dump(obj, fp, indent=2)