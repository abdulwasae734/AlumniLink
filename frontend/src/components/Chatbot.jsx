import React, { useState } from 'react';
import axios from 'axios';
import Markdown from 'react-markdown'
import "./chatbot.css"

const Chatbot = () => {
    const [userMessage, setUserMessage] = useState('');
    const [chatHistory, setChatHistory] = useState([]);

    const sendMessage = async () => {
        if (userMessage.trim() === '') return;

        // Add user message to chat history
        const updatedHistory = [...chatHistory, { sender: 'user', message: userMessage }];
        setChatHistory(updatedHistory);

        // Make an API call to FastAPI with the message and history
        try {
            const response = await axios.post('http://localhost:8000/chat', {
                message: userMessage,
                history: updatedHistory.map(chat => ({
                    role: chat.sender === 'user' ? 'user' : 'bot',
                    message: chat.message,
                })),
            });

            // Add bot response to chat history
            setChatHistory([...updatedHistory, { sender: 'bot', message: response.data.response }]);
        } catch (error) {
            console.error('Error sending message:', error);
        }

        // Clear input
        setUserMessage('');
    };

    return (
        <div className="chatbot">
            <div className="chat-window">
                {chatHistory.map((chat, index) => (
                    <div key={index} className={`chat-message ${chat.sender}-message`}>
                        {chat.sender === 'user' ? 'You' : 'Bot'} <Markdown>{chat.message}</Markdown>
                    </div>
                ))}
            </div>
            <div className="input">
            <input
                type="text"
                value={userMessage}
                onChange={(e) => setUserMessage(e.target.value)}
                placeholder="Type your message"
            />
            <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chatbot;