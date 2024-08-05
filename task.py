from crewai import Task
from agent import researcher, explainer

def create_research_task(anime_name, focus_areas):
    research_description = f"Research the anime '{anime_name}' using Wikipedia. If not found, use DuckDuckGo to find the most relevant information. Focus on: {', '.join(focus_areas)}. Provide only brief, key points."
    return Task(
        description=research_description,
        agent=researcher,
        expected_output=f"Brief key points about {anime_name}, focusing on {', '.join(focus_areas)}."
    )

def create_explain_task(anime_name, focus_areas):
    explain_description = f"Using the research provided, create a very concise explanation of the anime '{anime_name}', focusing specifically on: {', '.join(focus_areas)}. Limit your response to 3-4 sentences per focus area."
    return Task(
        description=explain_description,
        agent=explainer,
        expected_output=f"A very concise explanation of {anime_name}, focusing on {', '.join(focus_areas)}."
    )