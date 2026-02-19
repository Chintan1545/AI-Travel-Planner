# 🌍 AI Travel Planner 

An AI-powered Travel Planner that generates structured multi-day itineraries using LLMs and exports them as timed calendar events (.ics format) compatible with **Google Calendar**, **Microsoft Outlook**, and other calendar apps.

Built using:

* 🧠 LLM API from **Groq**
* 🎨 Streamlit UI
* 📅 iCalendar (.ics) export
* 🐍 Conda environment

---

## 🚀 Features

* Generate AI-based multi-day travel itinerary
* Structured output (Day-wise with Morning / Afternoon / Evening)
* Convert itinerary into timed calendar events
* Download `.ics` file
* Import directly into Google Calendar
* Free-tier compatible using Groq API

---

## 🏗️ Architecture

```
User Input (Destination + Days)
        ↓
Groq LLM (LLaMA 3 Model)
        ↓
Structured Itinerary
        ↓
Regex Parsing (Day + Time Blocks)
        ↓
iCalendar Generator
        ↓
Download .ics File
        ↓
Import into Calendar App
```

---

## 📦 Tech Stack

* Python 3.10
* Streamlit
* Groq API (LLaMA 3 70B)
* python-dotenv
* icalendar
* tzdata

---

## ⚙️ Installation Guide (Conda Recommended)

### 1️⃣ Create Conda Environment

```bash
conda create -n travel_groq python=3.10 -y
conda activate travel_groq
```

### 2️⃣ Install Dependencies

```bash
pip install streamlit groq icalendar python-dotenv tzdata
```

(Windows users may need:)

```bash
conda install -c conda-forge tzdata -y
```

---

## 🔑 Setup API Key

Create a `.env` file in project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key from:
[https://console.groq.com](https://console.groq.com)

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📅 How Calendar Export Works

The system:

1. AI generates itinerary in format:

```
Day 1:
Morning: ...
Afternoon: ...
Evening: ...
```

2. Regex extracts:

   * Day numbers
   * Time blocks

3. Time Mapping:

| Block     | Time         |
| --------- | ------------ |
| Morning   | 9 AM – 12 PM |
| Afternoon | 2 PM – 5 PM  |
| Evening   | 6 PM – 9 PM  |

4. Events are converted into `.ics` format using iCalendar library.

5. User downloads and imports into Google Calendar.

---

## 📂 Project Structure

```
AI-Travel-Planner/
│
├── ai_travel_planner.py
├── .env
├── README.md
└── requirements.txt
```

---

## 💡 Example Output

```
Day 1:
Morning: Visit Eiffel Tower
Afternoon: Explore Louvre Museum
Evening: Seine River Cruise
```

Calendar will show:

* 9:00–12:00 → Day 1 - Morning
* 2:00–5:00 → Day 1 - Afternoon
* 6:00–9:00 → Day 1 - Evening

---

## 🎯 Learning Outcomes

* LLM API Integration
* Prompt Engineering
* Regex Parsing
* Timezone Handling
* iCalendar File Generation
* Streamlit UI Development
* Conda Environment Management

---

## 🧠 Future Improvements

* Add hotel check-in events
* Add flight schedule events
* Add reminder notifications (VALARM)
* Add weather API integration
* Add budget estimation
* Deploy on cloud (Render / Streamlit Cloud)
* Convert to FastAPI backend

---

## 👨‍💻 Author

**Chintan Dabhi**
MCA (AI & ML) Student
AI/ML & Generative AI Enthusiast

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub!

---
