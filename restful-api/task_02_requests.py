#!/usr/bin/python3
"""
Bu modul 'requests' kitabxanası vasitəsilə API-dan məlumatları 
çəkmək və onları emal etmək üçün funksiyaları ehtiva edir.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    JSONPlaceholder API-dan postları çəkir, status kodunu 
    və uğurlu olarsa bütün postların başlıqlarını (title) çap edir.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Status kodunu çap edirik
    print("Status Code: {}".format(response.status_code))
    
    # Əgər sorğu uğurludursa (200 OK)
    if response.status_code == 200:
        posts = response.json()  # JSON məlumatını Python siyahısına çeviririk
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    JSONPlaceholder API-dan postları çəkir və onları 'id', 'title', 'body' 
    sütunları olmaqla 'posts.csv' faylına yadda saxlayır.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Sadəcə bizə lazım olan dataları (id, title, body) seçib yeni siyahı yaradırıq
        data_to_save = [
            {'id': post.get('id'), 'title': post.get('title'), 'body': post.get('body')} 
            for post in posts
        ]
        
        # Məlumatları CSV faylına yazırıq
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            # DictWriter lüğətləri (dictionaries) CSV formatına salmaq üçün ən ideal alətdir
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()  # Sütun adlarını (başlıqları) yazır
            writer.writerows(data_to_save)  # Bütün datanı sətir-sətir fayla yerləşdirir
