#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Siyahıdakı bütün unikal tam ədədləri bir dəfə toplamaqla cəmi hesablayır.
    
    Args:
        my_list: Tam ədədlərdən ibarət siyahı.
        
    Returns:
        Unikal ədədlərin cəmi.
    """
    
    # set(my_list) bütün təkrarlanan elementləri silir
    # sum() isə həmin unikal elementləri toplayır
    
    return sum(set(my_list))
