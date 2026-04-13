#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Yalnız bir çoxluqda mövcud olan elementlərin çoxluğunu qaytarır.
    
    Args:
        set_1: Birinci çoxluq
        set_2: İkinci çoxluq
        
    Returns:
        Hər iki çoxluğun simmetrik fərqi.
    """
    
    # '^' operatoru simmetrik fərqi hesablayır: (set_1 - set_2) | (set_2 - set_1)
    # Alternativ olaraq set_1.symmetric_difference(set_2) istifadə edilə bilər.
    
    return set_1 ^ set_2
