import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Initialize FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client using API key from environment
client = Groq(api_key="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")

# Define the request body model
class MessageRequest(BaseModel):
    message: str
    history: List[dict]  # Add history to the request model

# Function to interact with Groq LLM
def get_groq_response(user_message: str, chat_history: List[dict]) -> str:
    try:
        # Build message history for the LLM
        messages = [{"role": "user", "content": msg["message"]} for msg in chat_history]
        messages.append({"role": "user", "content": user_message})
        
        # Call Groq's chat completion endpoint
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",  # Example model
        )
        
        # Extract and return the response from Groq
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Handle errors and return a fallback message
        return f"Error: {str(e)}"

# Create a POST endpoint to handle incoming chat requests
@app.post("/chat")
async def chat(message: MessageRequest):
    bot_response = get_groq_response(message.message, message.history)
    return {"response": bot_response}