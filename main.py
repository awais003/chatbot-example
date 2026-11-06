import os
from dotenv import load_dotenv
from google import genai

# load env variables
load_dotenv()

# initialize gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_GEN_API_KEY"))

chat = client.chats.create(model="gemini-3.5-flash-lite")

print("===Pyton AI Chat===")
print("Type 'exit' to quite\n")

while True:
    # get user input
    question = input("You:")

    # eixt chatbot
    if question.lower() == "exit":
        print("AI: Goodbyte")
        break

    try:
        response = chat.send_message(question)
        
        # Display AI response
        print("AI:", response.text, "\n")
    except Exception as e:
        print("Error", e)


