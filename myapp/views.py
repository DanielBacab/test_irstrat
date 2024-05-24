from django.shortcuts import render
import requests


def obtener_personajes():
    url = "https://rickandmortyapi.com/api/character"
    parametros = {'page': 1}
    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()
    return datos['results'][:6] #Aqui limitamos a 6 los personajes, aunque se pidio 5, se ve mas estetico con 6

def obtener_info_personajes(personajes):
    info_personajes = []
    for personaje in personajes:
        nombre = personaje['name']
        origen = personaje['origin']['name']
        imagen_url = personaje['image']
        info_personajes.append({'nombre': nombre, 'origen': origen, 'imagen_url': imagen_url})
    return info_personajes

def mostrar_personajes(request):
    # Se llama a esta funcion que tiene la peticion GET para llamar a la API
    personajes = obtener_personajes()
    info_personajes = obtener_info_personajes(personajes)
    return render(request, 'myapp/index.html', {'info_personajes': info_personajes})