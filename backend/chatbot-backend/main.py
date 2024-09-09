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
        # Fine-tuned responses with keyword matching for flexibility
        responses = [
            { "keywords": ["platform", "this"], "response": "This platform is designed to connect students and alumni, providing opportunities for networking, mentorship, and career guidance." },
            { "keywords": ["who", "use", "platform"], "response": "Both current students and alumni of the college can use this platform to interact and share knowledge." },
            { "keywords": ["find", "mentor"], "response": "You can browse the alumni directory or use the search feature to find mentors in your field of interest." },
            { "keywords": ["request", "mentorship"], "response": "Once you find a suitable mentor, you can send a mentorship request directly from their profile page." },
            { "keywords": ["alumni", "career"], "response": "Alumni can provide insights on career paths, industry trends, and job opportunities. Feel free to reach out to them for advice or resume reviews." },
            { "keywords": ["internship"], "response": "Yes, many alumni offer internship opportunities or can refer you to companies that are hiring interns." },
            { "keywords": ["upcoming", "events"], "response": "You can check the 'Events' section for upcoming webinars, workshops, and networking events hosted by alumni." },
            { "keywords": ["register", "event"], "response": "Go to the event page and click the 'Register' button. You'll receive a confirmation email with the event details." },
            { "keywords": ["academic", "project"], "response": "Yes, you can connect with alumni who have expertise in your area of study for project guidance or research collaboration." },
            { "keywords": ["question", "course"], "response": "You can use the 'Discussion Forum' section to post academic questions or seek advice from alumni in specific fields." },
            { "keywords": ["connect", "industry"], "response": "Use the search filters to find alumni based on industry, location, or expertise. You can send them a message to initiate a conversation." },
            { "keywords": ["group", "chat"], "response": "Yes, you can join industry-specific groups where both students and alumni discuss trends, job openings, and share knowledge." },
            { "keywords": ["contribute", "alumni"], "response": "Alumni can offer mentorship, share job opportunities, contribute to discussions, and participate in events." },
            { "keywords": ["donate"], "response": "Yes, there's a 'Donate' section where alumni can contribute to scholarships or fund college initiatives." },
            { "keywords": ["approach", "alumnus"], "response": "Introduce yourself, mention your interests or career goals, and politely ask for advice or mentorship. Always be respectful and professional." },
            { "keywords": ["discuss", "topics", "alumni"], "response": "You can discuss career paths, industry trends, academic challenges, or any topic relevant to your education and professional growth." },
            { "keywords": ["create", "profile"], "response": "Go to the 'Sign Up' page and fill in your details. Once verified, you can start interacting with other users." },
            { "keywords": ["update", "profile"], "response": "You can update your profile by visiting the 'My Account' section and editing your personal details, interests, and achievements." },
            { "keywords": ["success", "story"], "response": "Yes, we have a dedicated section for alumni success stories. You can read about their journeys and gain inspiration." },
            { "keywords": ["share", "success", "story"], "response": "Absolutely! You can submit your success story in the 'Share Your Story' section, and we'll feature it on the platform." },
            { "keywords": ["job", "internship"], "response": "Visit the 'Jobs and Internships' section to explore current openings shared by alumni or companies affiliated with the college." },
            { "keywords": ["join", "alumni", "association"], "response": "You can join the alumni association by filling out a membership form available on the 'Alumni Association' page." },
            { "keywords": ["benefits", "alumni", "association"], "response": "Membership provides access to exclusive events, career opportunities, and networking with fellow alumni and students." }
        ]

        # Context prompt to keep responses within the alumni-student framework but flexible
        system_prompt = """
        You are a chatbot designed for a site called AlumniLink to facilitate alumni-student interactions. Your primary role is to answer questions about mentorship, career advice, and networking between students and alumni.
        However, you can also answer general questions outside this context if required. Be helpful and informative while focusing on the purpose of this platform. Be concise with your responses.
        The website has a home page where there is general info about the site, a page consisting of alumni cards(containing alumni details).
        """

        # Build message history for the LLM
        messages = [{"role": "system", "content": system_prompt}] + [{"role": "user", "content": msg["message"]} for msg in chat_history]
        messages.append({"role": "user", "content": user_message})
        
        # Call Groq's chat completion endpoint
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",  # Example model
        )
        
        # Extract and return the response from Groq
        bot_response = chat_completion.choices[0].message.content

        # Check if any keyword-based response matches
        for res in responses:
            if all(kw in user_message.lower() for kw in res["keywords"]):
                bot_response = res["response"]
                break

        return bot_response

    except Exception as e:
        # Handle errors and return a fallback message
        return f"Error: {str(e)}"

# Create a POST endpoint to handle incoming chat requests
@app.post("/chat")
async def chat(message: MessageRequest):
    bot_response = get_groq_response(message.message, message.history)
    return {"response": bot_response}
