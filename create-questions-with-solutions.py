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

#Create Questions
number = """
10
"""

subject = """
math
"""

difficulty = """
hard
"""

grade = """
grade 12
"""

prompt = f"""
Create {number} {subject} questions for {grade}. The difficulty level is {difficulty}
"""
response = get_completion(prompt)
print(response)

#Create Questions + solution
prompt = f"""
Create {number} {subject} questions for {grade}. The difficulty level is {difficulty}.
Please also provide the solution for each question.
"""
response = get_completion(prompt)
print(response)

#Check a given solution if it's correct or not
Question = """
I'm building a solar power installation and I need help \
working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
"""
    
Given_solution = """
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""

prompt = f"""
Your task is to determine if a given solution is correct or not.
To solve the problem do the following:
1. First, work out your own solution to the problem. 
2. Then compare your solution to the given solution and evaluate if the given solution is correct or not. 
Don't decide if the given solution is correct until you have done the problem yourself.

Question: {Question} 
Given solution: {Given_solution}

Answer using the following format:
Actual solution:
```
```
Is the given solution the same as actual solution just calculated:
```
yes or no
```
Correct/Incorrect:
```
correct or incorrect
```

Actual solution:
"""
response = get_completion(prompt)
print(response)
