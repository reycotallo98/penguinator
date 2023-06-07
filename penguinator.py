import subprocess
import openai
import os

openai.api_key = #TU APIKEY

control = True


def preguntar(prompte):

    respuesta = openai.Completion.create(
        engine='text-davinci-003',  # Puedes cambiar el motor según tus necesidades
        prompt="Escribeme entre punto y coma el comando que debo utilizar en linux para " + prompte + "y entre * la explicación " +
               "del mismo",
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




while control:
    subprocess.call("clear")
    frasedia = subprocess.call("fortune")
    subprocess.call("cowsay", "-t", "-f", "tux", frasedia + "¿en que puedo ayudarte?")
    prompt = input("Escribe tu consulta sobre linux, si quieres salir escribe 'N'")
    if prompt == "N":
        control = False
    else:
        subprocess.call("cowsay", "-t", "-f", "tux", preguntar(prompt))
