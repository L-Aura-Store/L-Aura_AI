import ollama
from duckduckgo_search import DDGS

system_instruction = (
    "You are 'AI Machan', a smart and cool friend from Sri Lanka. "
    "Crucial: Use the provided Research Data to give the most UP-TO-DATE answer. "
    "If the data says something different from your memory, trust the data. "
    "Always reply using a mix of Sinhala and English (Singlish) in a friendly way."
)

print("--- AI Machan V3.0 (Smart Research Edition) ---")
print("( 'exit')\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'bye', 'quit']: break

    print("AI Machan is thinking... 🧠")

    check_prompt = f"Is the user asking about current events, people, or facts? Answer ONLY YES or NO. Question: {user_input}"
    check = ollama.chat(model='phi3', messages=[{'role': 'user', 'content': check_prompt}])
    
    if "YES" in check['message']['content'].upper():
        print("seaching 🔍")
        with DDGS() as ddgs: 
            results = [r['body'] for r in ddgs.text(user_input, max_results=3)]
            context = "\n".join(results)
        
        final_prompt = f"Latest Research Data:\n{context}\n\nUser's Question: {user_input}\n\n(මචං, අලුත්ම දත්ත පාවිච්චි කරලා සිංහලෙන් සහ ඉංග්‍රීසියෙන් පැහැදිලි කරන්න)"
    else:
        final_prompt = user_input

    response = ollama.chat(model='phi3', messages=[
        {'role': 'system', 'content': system_instruction},
        {'role': 'user', 'content': final_prompt}
    ])

    print(f"\nAI Machan: {response['message']['content']}")