import tkinter as tk
import requests
import random
from io import BytesIO
from PIL import Image, ImageTk

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            nombre = data["name"].capitalize()
            numero = data["id"]
            tipos = [tipos["type"]["name"] for tipos in data["types"]]
            ataque = data["stats"][1]["base_stat"]  # Se obtiene el ataque base

            resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipos: {', '.join(tipos)}\nAtaque: {ataque}"

            imagen_url = data["sprites"]["front_default"]
            response_imagen = requests.get(imagen_url)
            imagen = Image.open(BytesIO(response_imagen.content))
            imagen = imagen.resize((200, 200))  # Redimensiona la imagen a 200x200
            foto = ImageTk.PhotoImage(imagen)
            label_imagen.config(image=foto)
            label_imagen.image = foto
        else:
            resultado = f"No se encontró el Pokémon '{nombre_pokemon}'"
            label_imagen.config(image=None)
    except requests.exceptions.RequestException as e:
        resultado = f"Error al conectar con la API: {str(e)}"
        label_imagen.config(image=None)

    label_resultado.config(text=resultado)

def buscar_poke_aleatorio():
    random_poke = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{random_poke}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            nombre = data["name"].capitalize()
            numero = data["id"]
            tipos = [tipos["type"]["name"] for tipos in data["types"]]

            resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipos: {', '.join(tipos)}"

            imagen_url = data["sprites"]["front_default"]
            response_imagen = requests.get(imagen_url)
            imagen = Image.open(BytesIO(response_imagen.content))
            imagen = imagen.resize((200, 200))
            foto = ImageTk.PhotoImage(imagen)
            label_imagen.config(image=foto)
            label_imagen.image = foto
        else:
            resultado = "No se encontró Pokémon"
            label_imagen.config(image=None)
    except requests.exceptions.RequestException as e:
        resultado = f"Error al conectar con la API: {str(e)}"
        label_imagen.config(image=None)

    label_resultado.config(text=resultado)

window = tk.Tk()
window.title("Busca tu Pokémon")

label_pokemon = tk.Label(window, text="Ingresa el nombre del Pokémon")
label_pokemon.pack()

entry_pokemon = tk.Entry(window)
entry_pokemon.pack()

button_buscar = tk.Button(window, text="Buscar", command=buscar_pokemon)
button_buscar.pack()

button_random = tk.Button(window, text="Buscar Aleatorio", command=buscar_poke_aleatorio)
button_random.pack()

label_resultado = tk.Label(window, text="", wraplength=300)
label_resultado.pack()

label_imagen = tk.Label(window)
label_imagen.pack()

window.mainloop()