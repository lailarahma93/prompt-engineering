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
WHAT = 'Fire'
WHO = '5 people'
WHERE = 'Nusantara office building 3rd floor, Jakarta'
WHEN = 'November 4th'
WHY = 'electrical short circuit'
HOW = 'it is still unknown how the short circuit happened.'
prompt = f"""Given a 5W1H information, write as a news writer, writing a hard news in a professional tone.

What: {WHAT}
Who: {WHO}
Where: {WHERE}
When: {WHEN}
Why: {WHY}
How: {HOW}

Write news with only informations provided above."""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)
