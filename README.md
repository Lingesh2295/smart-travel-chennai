# 🚍 Smart Travel Chennai  
### AI-Based Sustainable Urban Travel Assistant

Smart Travel Chennai is an AI-powered web application that helps users make informed and sustainable travel decisions within Chennai. The system allows users to enter a source and destination in natural language and receive estimated travel time and cost across multiple transport modes such as Metro, Bus, Auto, and Cab — all in one place.

This project focuses on responsible, lightweight AI and promotes eco-friendly urban mobility by encouraging public transport usage through transparent comparison.

---

## 🌍 Problem Statement

Urban commuters often rely on multiple applications to compare travel options, leading to confusion, inefficiency, and increased dependency on private vehicles. Existing platforms rarely present clear, side-by-side comparisons of time and cost for different transport modes.

Smart Travel Chennai addresses this gap by providing a single conversational interface that simplifies travel planning while promoting sustainable commuting choices.

---

## 💡 Solution Overview

- Users interact with a chat-based interface
- Natural language input is processed to extract source and destination
- Distance and base travel time are fetched using Google Maps Directions API
- AI-based heuristic logic estimates travel time and cost for each transport mode
- Results are presented clearly to support informed decision-making

The system acts as a decision-support assistant rather than a real-time tracker, ensuring transparency and ethical AI usage.

---

## 🤖 AI Elements Used

- Natural Language Processing (NLP) for understanding user queries  
- Heuristic-based AI logic for estimating travel time and cost  
- AI-based Decision Support System for comparing transport modes  
- REST API integration for data retrieval and communication  

---

## 🛠️ Technologies Used

- Python  
- FastAPI  
- REST APIs  
- Google Maps Directions API  
- HTML, CSS, JavaScript  
- Git & GitHub  
- Uvicorn  

---

## 🎯 Target Users

- Daily commuters in Chennai  
- Students and office-goers  
- New residents and visitors  
- Users seeking sustainable travel options  

---

## 🌱 Sustainability Impact

- Encourages use of public and shared transport  
- Helps reduce traffic congestion and carbon emissions  
- Promotes smarter and more efficient urban mobility  
- Demonstrates responsible and explainable AI usage  

Aligned with **UN Sustainable Development Goal 11 – Sustainable Cities and Communities**.

---

## 📸 Key Features

- Conversational chatbot interface  
- Multi-mode transport comparison  
- Estimated travel time and cost  
- Clean and user-friendly UI  
- Lightweight and explainable AI logic  

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/chennai-travel-chatbot.git

# Navigate to backend folder
cd chennai-travel-chatbot/backend

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
