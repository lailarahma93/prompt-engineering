#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laila
"""

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

Language =  """Spanish"""
Level = """Beginners A1"""

prompt = f"""
Create a {Language} reading for {Level} level
"""
response = get_completion(prompt)
print(response)

#ANSWER:
#Mi nombre es María. Soy de España. Tengo veinte años. Vivo en Madrid con mi familia. Tengo un hermano y una hermana. Mi hermano se llama Juan y mi hermana se llama Ana. Mi padre se llama Carlos y mi madre se llama Laura. 

#Soy estudiante en la universidad. Estudio medicina. Me gusta mucho ayudar a las personas. Quiero ser médica en el futuro. 

#En mi tiempo libre, me gusta leer libros y ver películas. También me gusta salir con mis amigos. 

#Hablo español y inglés. Estoy aprendiendo francés en la escuela. 

#Me gusta mucho la comida española. Mi plato favorito es la paella. También me gusta comer tapas y churros con chocolate. 

#En verano, me gusta ir a la playa con mi familia. Me encanta nadar y tomar el sol. 

#Eso es todo sobre mí. ¡Espero que hayas disfrutado leyendo sobre mi vida!
