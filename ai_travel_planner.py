import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from icalendar import Calendar, Event
from datetime import datetime, timedelta, timezone
import re


# Load API Key

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Timed ICS Generator

def generate_ics_content(plan_text: str, start_date: datetime = None) -> bytes:
    cal = Calendar()
    cal.add("prodid", "-//AI Travel Planner//")
    cal.add("version", "2.0")

    if start_date is None:
        start_date = datetime.now(timezone.utc)

    day_pattern = re.compile(r"Day (\d+):(.*?)(?=Day \d+:|$)", re.DOTALL)
    days = day_pattern.findall(plan_text)

    time_blocks = {
        "Morning": (9, 12),
        "Afternoon": (14, 17),
        "Evening": (18, 21),
    }

    for day_num, day_content in days:
        day_num = int(day_num)
        current_date = start_date + timedelta(days=day_num - 1)

        for block_name, (start_hour, end_hour) in time_blocks.items():
            match = re.search(
                rf"{block_name}:(.*?)(?=(Morning|Afternoon|Evening|$))",
                day_content,
                re.DOTALL
            )

            if match:
                description = match.group(1).strip()

                event = Event()
                event.add("summary", f"Day {day_num} - {block_name}")
                event.add("description", description)

                start_datetime = current_date.replace(
                    hour=start_hour, minute=0, second=0, microsecond=0
                )
                end_datetime = current_date.replace(
                    hour=end_hour, minute=0, second=0, microsecond=0
                )

                event.add("dtstart", start_datetime)
                event.add("dtend", end_datetime)
                event.add("dtstamp", datetime.now(timezone.utc))

                cal.add_component(event)

    return cal.to_ical()


# Streamlit UI

st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("🌍 AI Travel Planner ")
st.caption("Generate smart travel plans and export to calendar")

destination = st.text_input("Where do you want to go?")
num_days = st.number_input("How many days?", min_value=1, max_value=15, value=5)

if "itinerary" not in st.session_state:
    st.session_state.itinerary = None


# Generate Itinerary

if st.button("Generate Itinerary"):
    if destination:
        with st.spinner("Generating your travel plan..."):

            prompt = f"""
            Create a detailed {num_days}-day travel itinerary for {destination}.

            Structure strictly like this:

            Day 1:
            Morning: ...
            Afternoon: ...
            Evening: ...

            Continue same format for all days.
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a professional travel planner."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000,
            )

            itinerary = response.choices[0].message.content
            st.session_state.itinerary = itinerary

        st.success("Itinerary Generated Successfully!")
        st.write(itinerary)


# Download ICS

if st.session_state.itinerary:
    ics_content = generate_ics_content(st.session_state.itinerary)

    st.download_button(
        label="📅 Download Timed Calendar (.ics)",
        data=ics_content,
        file_name="travel_itinerary.ics",
        mime="text/calendar"
    )
