
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="✈️"
)

st.title("✈️ GenAI Travel Assistant")
st.write("Your AI-powered travel planning companion!")

# Connect to Gemini
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

destination = st.text_input(
    "Where do you want to travel?"
)

days = st.number_input(
    "How many days?",
    min_value=1,
    max_value=30,
    value=3
)

budget = st.text_input(
    "Enter your approximate budget"
)

if st.button("Generate Travel Plan"):
    if destination and budget:
        prompt = f"""
        Act as a helpful travel assistant.

        Create a travel itinerary for:
        Destination: {destination}
        Duration: {days} days
        Budget: {budget}

        Include:
        1. Day-wise itinerary
        2. Popular tourist attractions
        3. Food recommendations
        4. Travel suggestions
        5. Budget planning

        Clearly mention that prices and opening
        hours should be verified before travelling.
        """

        try:
            with st.spinner("Creating your travel plan..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            st.subheader("Your Travel Itinerary")
            st.write(response.text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

    else:
        st.warning("Please enter your destination and budget.")
