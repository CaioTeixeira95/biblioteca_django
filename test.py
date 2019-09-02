import os
import json


title = input('Digite o título do livro: ')
isbn = input('Digite o ISBN: ')
author = input('Digite o autor: ')
print("""Escolha o gênero do livro:
1 - Ação
2 - Aventura
3 - Terror
4 - Suspense
5 - Drama
6 - Comédia
7 - Manga
8 - Quadrinhos""")

gender = int(input())
choice = ''

if gender == 1:
    choice = 'ac'
elif gender == 2:
    choice = 'ad'
elif gender == 3:
    choice = 'h'
elif gender == 4:
    choice = 'th'
elif gender == 5:
    choice = 'd'
elif gender == 6:
    choice = 'c'
elif gender == 7:
    choice = 'm'
elif gender == 8:
    choice = 'co'

os.system("curl -X POST http://127.0.0.1:8000/books/ -H 'content-type: application/json' -d '{}'".format(
        json.dumps({
            'title': title,
            'isbn': isbn,
            'author': author,
            'gender': choice,
        })
    )
)
