# 🚀 Smart AI Student Productivity Assistant

## 📌 Overview
This project is an AI-powered Smart Student Assistant designed to help students generate optimized study plans based on available time, subjects, and priorities. It uses intelligent decision-making and Google Gemini API to provide dynamic and practical study strategies.

---

## 🎯 Chosen Challenge
Election Process Education (Adapted to Educational Productivity & Planning)

---

## 🧠 Approach & Logic
The system takes user input such as:
- Number of days available
- Subjects to study

It then:
- Uses AI (Google Gemini API) to analyze the input
- Generates a structured and optimized study plan
- Provides time allocation, prioritization, and tips

This ensures dynamic, context-aware decision-making rather than static outputs.

---

## ⚙️ How It Works
1. User sends input via API (days + subjects)
2. Backend processes input using Flask
3. Prompt is sent to Gemini API
4. AI generates a smart study plan
5. Response is returned in JSON format

---

## ☁️ Google Services Used
- Google Gemini API (AI-based content generation)
- (Optional) Google Cloud Run (for deployment)

---

## ✅ Features
- AI-powered smart assistant using Google Gemini API
- Dynamic and context-aware study plan generation
- REST API-based backend
- Real-time intelligent responses
- Simple and scalable design

---

## 🛠️ Tech Stack
- Python (Flask)
- Requests (API handling)
- Google Gemini API
- Docker (for deployment)
- Google Cloud Run (optional deployment)

---

## 📌 API Endpoint

### POST /plan

#### Request Body:
```json
{
  "days": 3,
  "subjects": ["Math", "Physics", "Chemistry"]
}
