import google.generativeai as genai

key = "AIzaSyA-TtYl_35Ha3elcwhX39SCHtRivQBCNh4"#input("Enter your API key: ")

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1")
prompt = "I AM SO FUCKING DONE I CANNOT FUCKING STAND"
response = model.generate_content(prompt)
print(response.text)