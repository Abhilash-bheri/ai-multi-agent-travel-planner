# ✈️ AI Multi-Agent Travel Planner


An intelligent AI-powered Travel Planner built using **LangGraph**, **Google Gemini**, **Tavily Search**, and **AviationStack API**.

The application uses a **multi-agent architecture** where specialized AI agents collaborate to generate complete travel plans including flight suggestions, hotel recommendations, and personalized itineraries.

## 🌐 Live Demo

https://ai-multi-agent-travel.streamlit.app

---

## 🚀 Features

- Multi-Agent AI Workflow using LangGraph
- Intelligent Intent Extraction
- Flight Search using AviationStack API
- Hotel Recommendations using Tavily Search
- AI-generated Personalized Travel Plans
- Beautiful Streamlit Interface
- Download Travel Plan
- Modular Agent Architecture
- Production Deployment on Streamlit Community Cloud

---

## 🧠 Multi-Agent Workflow

```text
User Request
      │
      ▼
Intent Agent
      │
 ┌────┴────┐
 ▼         ▼
Flight   Hotel
 Agent     Agent
      │
      ▼
Planner Agent
      │
      ▼
Final Travel Plan
```

---

## 🛠 Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini 2.5 Flash
- Tavily Search API
- AviationStack API
- Streamlit
- Pydantic
- dotenv

---

## 📂 Project Structure

```
.
├── app.py
├── main.py
├── tools
│   ├── flight_tool.py
│   └── tavily_tool.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Abhilash-bheri/ai-multi-agent-travel-planner.git
```

Move into the project

```bash
cd ai-multi-agent-travel-planner
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
GOOGLE_API_KEY=your_key
TAVILY_API_KEY=your_key
AVIATIONSTACK_API_KEY=your_key
```

Run

```bash
streamlit run app.py
```

---

## 💡 Example Prompt

```
Plan a 5-day trip from Hyderabad to Goa with a budget of ₹30,000.

Include:

• Flight options
• Best hotels
• Tourist attractions
• Food recommendations
• Day-wise itinerary
• Estimated expenses
```

---

## 🎯 Architecture

- Intent Agent
- Flight Agent
- Hotel Agent
- Planner Agent

Each agent has a single responsibility and collaborates using LangGraph's workflow orchestration.

---

## 📸 Demo

Add screenshots here.

```
assets/home.png

assets/result.png
```

---

## 🌍 Live Application

https://ai-multi-agent-travel.streamlit.app

---

## Future Improvements

- Google Maps Integration
- Weather Forecast
- Budget Optimization
- Restaurant Recommendations
- PDF Export
- Multi-city Trips
- Voice Input
- Currency Conversion
- Interactive Maps
- Travel Cost Analytics

---

## Author

**Abhilash Bheri**

LinkedIn:
https://linkedin.com/in/Abhilash-bheri

GitHub:
https://github.com/Abhilash-bheri

---

⭐ If you found this project useful, consider giving it a star.
