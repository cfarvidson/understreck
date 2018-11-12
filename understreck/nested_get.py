# -*- coding: utf-8 -*-
from .exceptions import InvalidArgumentError


def nested_get(input_dict, nested_key):
    """Get a subkey from a dict

    This will return a subkey from a dictionary. 
    It solves a problem when having to perform safe get on nested dictionaries.
    
    Arguments:
        input_dict {dict} -- The dictionary to perform the get on
        nested_key {str, list, tuple} -- The key can be or dot delimited string or list/tuple.
    
    Returns:
        Object or None -- The value of the key or None
    """
    if not isinstance(nested_key, (str, list, tuple)):
        raise InvalidArgumentError("The nested_key is not the correct type")
    if not isinstance(input_dict, dict):
        raise InvalidArgumentError("The input_dict is not the correct type")

    normalized_nested_key = None
    if isinstance(nested_key, str):
        normalized_nested_key = nested_key.split(".")
    elif isinstance(nested_key, (list, tuple)):
        normalized_nested_key = nested_key

    internal_dict_value = input_dict
    for k in normalized_nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value


get = nested_get
