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

Genre =  """fairy"""
Main_Character = """a little girl"""
Other_Characters = """a unicorn, a deer, a little boy, and a witch"""
Location = """German village"""
Time = """medieval age"""
Reader = """toddlers"""
Foreign_Language = """Korean"""
Desired_Language = """English"""

#Prompt 1 (create story)
prompt = f"""
Create a {Genre} story with {Main_Character} as the main character. \
The other characters include {Other_Characters}. \
The setting is {Location} during {Time}. This story is for {Reader}.
"""
response = get_completion(prompt)
print(response)

#Prompt 2 (create story in foreign language + translation in the desired language)
prompt = f"""
Create a {Genre} story in {Foreign_Language} with {Main_Character} as the main character. \
The other characters include {Other_Characters}. \
The setting is {Location} during {Time}. This story is for {Reader}. \
Provide the {Desired_Language} translation.
"""
response = get_completion(prompt)
print(response)
