# 🚍 Smart Travel Chennai
### AI-Based Sustainable Urban Travel Assistant

Smart Travel Chennai is a web-based travel assistant designed to help commuters make smarter, more affordable, and sustainable travel decisions within Chennai.

The application allows users to enter a source and destination through a conversational interface and compare estimated travel time and cost across multiple transportation modes, including **Metro, Bus, Auto, and Cab**.

By combining rule-based Natural Language Processing (NLP), heuristic decision logic, FastAPI, and the Google Maps Directions API, the application provides a centralized platform for urban travel planning.

## 🌍 Problem Statement

Urban commuters often use multiple applications to compare transportation options, making travel planning time-consuming and inconvenient.

Additionally, many travel platforms do not provide a simple side-by-side comparison of estimated time and cost across different transportation modes.

Smart Travel Chennai addresses this problem by offering a unified, conversational travel assistant that supports informed and sustainable commuting decisions.

## 💡 Proposed Solution

The application follows a straightforward workflow:

1. The user enters a travel query containing a source and destination.
2. Rule-based NLP processes the query to identify travel locations.
3. The Google Maps Directions API provides route distance and base travel duration.
4. Heuristic logic estimates travel time and cost for different transportation modes.
5. The application presents the results through a web-based interface.

**Note:** Travel times and fares are estimates, not guaranteed live transit schedules or official fare quotations.

## ✨ Key Features

- **Conversational Interface:** Users can enter travel queries in natural language.
- **Multi-Mode Comparison:** Compare Metro, Bus, Auto, and Cab options.
- **Travel Time Estimation:** Calculate approximate travel durations.
- **Fare Estimation:** Estimate transportation costs using heuristic logic.
- **Google Maps Integration:** Retrieve route distance and duration information.
- **RESTful Backend:** Process requests through FastAPI endpoints.
- **Sustainable Travel Planning:** Support public transport awareness and informed travel choices.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI |
| API Server | Uvicorn |
| AI/NLP | Rule-based NLP, heuristic logic |
| External API | Google Maps Directions API |
| Frontend | HTML, CSS, JavaScript |
| API Communication | REST APIs, Requests |
| Configuration | python-dotenv |
| Version Control | Git, GitHub |

## 🧠 AI and Decision-Support Approach

Smart Travel Chennai uses lightweight, explainable AI techniques rather than a computationally intensive machine-learning model.

**Natural Language Processing (NLP)**

Rule-based text processing helps identify the source and destination from user inputs.

**Heuristic Estimation**

Predefined rules and calculations estimate travel duration and transportation costs across available travel modes.

**Decision Support**

The application displays comparable transportation options, helping users evaluate estimated cost, time, and commuting preferences.

This approach emphasizes transparency, simplicity, and efficient resource utilization.

## 📁 Project Structure

```text
smart-travel-chennai/
│
├── backend/
│   ├── static/
│   │   ├── index.html
│   │   ├── script.js
│   │   ├── style.css
│   │   └── images/
│   │
│   ├── ai.py
│   ├── fares.py
│   ├── main.py
│   ├── maps.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

## ▶️ Installation and Local Setup

### Prerequisites

- Python installed on your system
- Git
- Google Maps API key with appropriate API access
- Internet connection for Google Maps API requests

### 1. Clone the Repository

```bash
git clone https://github.com/Lingesh2295/smart-travel-chennai.git
cd smart-travel-chennai
```

### 2. Create a Virtual Environment

```bash
python -m venv backend/venv
```

Activate it on Windows PowerShell:

```powershell
.\backend\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure Google Maps API

Create a `.env` file inside the `backend` directory.

```dotenv
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

Replace the placeholder with your own valid API key.

**Security:** Never commit your `.env` file or API credentials to GitHub.

### 5. Start the FastAPI Server

```bash
cd backend
uvicorn main:app --reload
```

By default, Uvicorn serves the application at:

`http://127.0.0.1:8000`

FastAPI's interactive API documentation is normally available at:

`http://127.0.0.1:8000/docs`

Open the web interface using the route configured in `main.py`.

## 📸 Application Screenshots

Add screenshots here to demonstrate:

- The conversational travel interface
- A sample source and destination query
- Transport mode comparison results
- Estimated fares and travel durations

## 🌱 Sustainability Impact

Smart Travel Chennai promotes awareness of sustainable urban transportation by:

- Encouraging consideration of public and shared transport
- Providing transparent comparisons between travel modes
- Supporting cost-conscious commuting decisions
- Demonstrating resource-efficient, explainable AI techniques

The project's objectives align with **United Nations Sustainable Development Goal 11: Sustainable Cities and Communities**.

## 👥 Target Users

- Daily commuters in Chennai
- College students and working professionals
- Tourists and new residents
- Users looking for affordable and sustainable travel options

## 🚀 Future Enhancements

- Real-time public transport schedule integration
- Improved conversational NLP capabilities
- Traffic-aware recommendations
- Carbon emission estimation for each travel mode
- Multilingual support, including Tamil
- More personalized route recommendations

## ⚠️ Limitations

- Fare estimates are heuristic and may differ from actual charges.
- Route information depends on Google Maps API availability and coverage.
- The system does not provide live tracking of public transport vehicles.
- Natural language understanding is rule-based and may not recognize every query format.

## 👨‍💻 Author

**Lingesh J**

GitHub: [Lingesh2295](https://github.com/Lingesh2295)

## 📌 Project Repository

[Smart Travel Chennai on GitHub](https://github.com/Lingesh2295/smart-travel-chennai)
