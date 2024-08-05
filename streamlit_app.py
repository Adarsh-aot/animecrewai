import streamlit as st
from crew import create_anime_crew

st.title("Anime Explainer")

anime_name = st.text_input("Enter the name of an anime:")

focus_areas = st.multiselect(
    "What would you like to know about this anime?",
    ["Plot", "Characters", "Themes", "Cultural impact", "Production history"],
    default=["Plot", "Characters", "Themes"]
)

if st.button("Explain Anime"):
    if anime_name and focus_areas:
        st.write(f"\nResearching {anime_name} with focus on: {', '.join(focus_areas)}")
        
        with st.spinner("Analyzing anime..."):
            anime_crew = create_anime_crew(anime_name, focus_areas)
            result = anime_crew.kickoff()
        
        st.subheader("Here's what I found:")
        st.write(result)
    else:
        st.warning("Please enter an anime name and select at least one focus area.")

st.sidebar.markdown("""
## About
This app uses AI to research and explain anime based on your interests.
It uses CrewAI with Groq's language model to generate explanations.
""")