import requests
import json


1

def comment(n):
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    n=(input("ingrese el numero del comentario:"))
    diccionario = {"comentario" : consulta[int(n)]['body']}
    return diccionario

n=0
print(comment(n))