"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as palm
palm.configure(api_key="YOUR API KEY")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
input = '90's'
input2 = 'someone that is just heart broken'
prompt = f"""Recommend me some {input} songs that are perfect for {input2}"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)

#ANSWER:
#1. **Torn** by Natalie Imbruglia 
#2. **All by Myself** by Celine Dion 
#3. **I Will Survive** by Gloria Gaynor 
#4. **Yesterday** by The Beatles 
#5. **One Sweet Day** by Mariah Carey and Boyz II Men 
#6. **Iris** by Goo Goo Dolls 
#7. **Don't Speak** by No Doubt 
#8. **My Heart Will Go On** by Celine Dion 
#9. **Missing You** by John Waite 
#10. **When You Say Nothing at All** by Alison Krauss 
