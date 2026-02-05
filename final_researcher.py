import ollama
from duckduckgo_search import DDGS

print("seaching 🔍")
search_query = "What is the latest news about AI in February 2026?"
with DDGS() as ddgs:
    results = [r['body'] for r in ddgs.text(search_query, max_results=2)]
    context = "\n".join(results)

print("AI එක පිළිතුර සකස් කරයි...")
prompt = f"Using this information: {context}\n\nQuestion: {search_query}"

response = ollama.chat(model='phi3', messages=[
    {'role': 'user', 'content': prompt}
])

print("\n--- AI Research Report ---")
print(response['message']['content'])