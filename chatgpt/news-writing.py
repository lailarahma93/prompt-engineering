#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 00:20:02 2023

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

WHAT =  """Fire"""
WHO = """5 people"""
WHERE = """Nusantara office building 3rd floor, Jakarta"""
WHEN = """November 4th"""
WHY = """electrical short circuit"""
HOW = """it is still unknown how the short circuit happened."""

prompt = f"""Given a 5W1H information, write as a news writer, writing a hard news in a professional tone.

What: {WHAT}
Who: {WHO}
Where: {WHERE}
When: {WHEN}
Why: {WHY}
How: {HOW}

Write news with only informations provided above."""
response = get_completion(prompt)
print(response)

#ANSWER:
#Fire Breaks Out at Nusantara Office Building, Leaving 5 People Injured

#Jakarta, November 4th - A fire erupted on the third floor of the Nusantara office building in Jakarta earlier today, resulting in injuries to five individuals. The incident was caused by an electrical short circuit, although the exact cause of the short circuit remains unknown.

#The blaze broke out at approximately [insert time] on the third floor of the Nusantara office building, located in [insert specific location]. The fire quickly spread, engulfing the area and causing panic among the occupants.

#Emergency services were immediately dispatched to the scene upon receiving distress calls. Firefighters worked tirelessly to extinguish the flames and evacuate the building. Paramedics provided medical assistance to the injured individuals, who were later transported to nearby hospitals for further treatment.

#Authorities have confirmed that five people sustained injuries during the incident. However, the severity of their injuries and their current condition remain undisclosed at this time. The identities of the victims have also not been released.

#Preliminary investigations have revealed that the fire was triggered by an electrical short circuit. However, the exact circumstances leading to the short circuit are yet to be determined. Authorities are conducting a thorough examination to ascertain the cause and prevent similar incidents in the future.

#The Nusantara office building has temporarily suspended operations as a result of the fire. Employees and tenants have been advised to stay away from the premises until further notice. The building management is working closely with the authorities to assess the extent of the damage and ensure the safety of the structure before allowing occupants to return.

#As investigations continue, authorities urge individuals to exercise caution and prioritize safety measures to prevent fire-related incidents. Further updates regarding the incident will be provided as more information becomes available.

###

#Note: This news article is a fictional creation and does not represent any real events or individuals.