from django.shortcuts import render
import requests


def obtener_personajes():
    url = "https://rickandmortyapi.com/api/character"
    parametros = {'page': 1}  # Obtener la primera página de resultados
    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()
    return datos['results'][:6]

def obtener_info_personajes(personajes):
    info_personajes = []
    for personaje in personajes:
        nombre = personaje['name']
        origen = personaje['origin']['name']
        imagen_url = personaje['image']
        info_personajes.append({'nombre': nombre, 'origen': origen, 'imagen_url': imagen_url})
    return info_personajes

def mostrar_personajes(request):
    # Obtener los personajes
    personajes = obtener_personajes()
    info_personajes = obtener_info_personajes(personajes)

    print("ACTIVADOOOOOOOOOOOOOOOO")  # Esto debería imprimir en la consola del servidor si la función se llama
    return render(request, 'myapp/index.html', {'info_personajes': info_personajes})