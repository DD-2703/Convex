"""
Contains all utilities related to searching a list / dictionary.
"""

def search(search_obj, obj: list) -> bool:
    """
    Performs a normal linear search. Can be replaced by a simple
    [search_obj] in [list] statement.
    Returns a boolean 
    """
    if search_obj in obj: return True
    return False

def int_binary_search(search_obj: int, sorted_obj: list) -> bool:
    """
    Recursive implementation of binary search.
    Returns a boolean. 
    """
    if sorted_obj[0] == search_obj: return True

    _convex_sorted_copy = sorted_obj
    del _convex_sorted_copy[0]
    _convex_list_middle = int(len(_convex_sorted_copy)/2)

    if _convex_sorted_copy[_convex_list_middle] == search_obj: return True

    if _convex_sorted_copy[_convex_list_middle] < search_obj:
        del _convex_sorted_copy[:_convex_list_middle]
        return int_binary_search(search_obj, _convex_sorted_copy)
    
    if _convex_sorted_copy[_convex_list_middle] > search_obj:
        del _convex_sorted_copy[_convex_list_middle:]
        return int_binary_search(search_obj, _convex_sorted_copy)

    return False
