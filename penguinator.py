import subprocess
import openai
import os

openai.api_key =#APIKEY

control = True


def preguntar(prompte):

    respuesta = openai.Completion.create(
        engine='text-davinci-003',  # Puedes cambiar el motor según tus necesidades
        prompt="Escribeme punto y coma y el comando que debo utilizar en linux para " + prompte ,
        max_tokens=200,  # Define la longitud máxima de la respuesta generada
        n=1,  # Número de respuestas que deseas obtener
        stop=None,  # Opcional: cadena de texto para detener la respuesta generada antes de que sea demasiado larga
        temperature=0.7,
        # Controla la aleatoriedad de las respuestas generadas (0.0 es más determinista, 1.0 más aleatorio)
        timeout=None  # Opcional: tiempo límite en segundos para la solicitud
    )

    if respuesta and len(respuesta.choices) > 0:
        return respuesta.choices[0].text.strip()
    else:
        return "No se recibió ninguna respuesta del modelo."



os.system("clear")

while control:
    os.system("cowsay -t -f tux ¿en que puedo ayudarte?")
    prompt = input("Escribe tu consulta sobre linux, si quieres salir escribe 'N'\n")
    os.system("clear")
    if prompt == "N":
        control = False
    else:
        pro = preguntar(prompt)
        os.system("cowsay -t -f tux "+ pro)
        os.system(pro)
