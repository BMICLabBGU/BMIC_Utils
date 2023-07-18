import os
import json
import yaml
import pickle
from easydict import EasyDict

def pickle_read(file_path: str):
    """
    De-serializes an object from a provided file path.
    
    :param file_path: The file path
    :return: the deserialized object from the provided file path.
    """

    with open(os.path.realpath(file_path), 'rb') as file:
        return pickle.load(file)


def pickle_write(obj, file_path: str):
    """
    Serializes an object and saves it as a pickle file.
    
    :param obj: The object that you want to serialize and write to a file. It can be any Python object
                    that is pickle-able, meaning it can be serialized using the `pickle` module
    :param file_path: The path to the file where the object will be serialized and saved
    """

    file_path = os.path.realpath(file_path)
    os.makedirs(os.path.split(file_path)[0], exist_ok=True)

    with open(file_path, 'wb',) as file:
        pickle.dump(obj, file)


def json_read(path: str, easy_dict: bool = True):
    """
    Reads a JSON file from the specified path and returns the contents as a
    dictionary, optionally converting it to an EasyDict object.
    
    :param path: The file path of the JSON file that you want to read. 
    :param easy_dic (optional)t: If set to `True`, the JSON object will be converted to an `EasyDict` object, defaults to True
    :return: The file at the specified path. 
    """
    with open(os.path.realpath(path), "r") as fp:
        obj = json.load(fp)

    if easy_dict:
        obj = EasyDict(obj)

    return obj


def json_write(obj, path: str, **kwargs):
    """
    Writes a Python object to a JSON file with specified formatting options.
    
    :param obj: A Python object that you want to write to a JSON file. 
    :param path: The file path where the JSON data will be written to.
    """
    path = os.path.realpath(path)
    os.makedirs(os.path.split(path)[0], exist_ok=True)

    if 'indent' not in kwargs:
        kwargs['indent'] = 2

    with open(path, 'w') as fp:
        json.dump(obj, fp, **kwargs)
        
def yaml_read(path: str, unsafe_load: bool = False, easy_dict: bool = True):
    """
    Reads a YAML file from the specified path and returns the contents as a
    dictionary, optionally converting it to an EasyDict object.
    
    :param path: The file path of the YAML file that you want to read. 
    :param easy_dic (optional)t: If set to `True`, the YAML object will be converted to an `EasyDict` object, defaults to True
    :return: The file at the specified path. 
    """
    with open(os.path.realpath(path), "r") as fp:
        if unsafe_load:
            obj = yaml.unsafe_load(fp)
        else:
            obj = yaml.safe_load(fp)

    if easy_dict:
        obj = EasyDict(obj)

    return obj


def yaml_write(obj, path: str):
    """
    Writes a Python object to a YAML file with specified formatting options.
    
    :param obj: A Python object that you want to write to a YAML file. 
    :param path: The file path where the YAML data will be written to.
    """
    with open(path, 'w') as fp:
        yaml.dump(obj, fp, indent=2)