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
input = 'why is the sky blue?'
prompt = f"""Explain about {input} for kids age below 5. Do not use difficult terms."""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)

#ANSWER:
#The sky is blue because of the way sunlight interacts with the Earth's atmosphere. 
#Sunlight is made up of all colors of the rainbow, but when it passes through the atmosphere, 
#the blue light is scattered more than the other colors. This is because blue light has a shorter wavelength than the other colors, 
#and shorter wavelengths are more easily scattered by particles in the atmosphere. The other colors of light are not scattered as much, 
#so they travel through the atmosphere to our eyes. This is why we see the sky as blue. 
