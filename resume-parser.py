import openai
import json

# Load your API key from an environment variable or secret management service
openai.api_key = 'your-api-key-here'

resume_content = """
[Insert your resume content here]
"""

prompt = f"""
You are a resume parser. Your task is to take the content of a resume and convert it into a JSON format. Here is the structure for the JSON format:

```json
{{
  "name": "",
  "contact": {{
    "email": "",
    "phone": "",
    "address": ""
  }},
  "summary": "",
  "experience": [
    {{
      "job_title": "",
      "company": "",
      "location": "",
      "start_date": "",
      "end_date": "",
      "description": ""
    }}
  ],
  "education": [
    {{
      "degree": "",
      "institution": "",
      "location": "",
      "graduation_year": ""
    }}
  ],
  "skills": []
}}

Please parse the following resume content:

{resume_content}

Return the parsed JSON.
"""

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1500
)

parsed_json = response.choices[0].text.strip()
parsed_data = json.loads(parsed_json)

print(json.dumps(parsed_data, indent=2))
