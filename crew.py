from crewai import Crew
from agent import researcher, explainer
from task import create_research_task, create_explain_task

def create_anime_crew(anime_name, focus_areas):
    research_task = create_research_task(anime_name, focus_areas)
    explain_task = create_explain_task(anime_name, focus_areas)

    anime_crew = Crew(
        agents=[researcher, explainer],
        tasks=[research_task, explain_task],
        verbose=True
    )

    return anime_crew