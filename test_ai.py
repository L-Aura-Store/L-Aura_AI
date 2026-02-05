import ollama

response = ollama.chat(model='phi3', messages=[
  {
    'role': 'user',
    'content': 'Hi, tell me one interesting fact about AI.',
  },
])
print(response['message']['content'])