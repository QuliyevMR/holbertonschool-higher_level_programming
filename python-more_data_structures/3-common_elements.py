#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    İki çoxluğun kəsişməsini (ortaq elementlərini) qaytaran funksiya.
    
    Args:
        set_1: Birinci çoxluq
        set_2: İkinci çoxluq
        
    Returns:
        Hər iki çoxluqda olan elementlərdən ibarət yeni bir çoxluq.
    """
    
    # Python-da '&' operatoru iki çoxluğun kəsişməsini tapır.
    # Alternativ olaraq set_1.intersection(set_2) istifadə etmək olar.
    
    return set_1 & set_2
