from crewai import Agent
import os
from langchain.agents import Tool
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Setup API keys if needed (not required for Wikipedia or DuckDuckGo)
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Initialize tools
wikipedia = WikipediaAPIWrapper()
search = DuckDuckGoSearchRun()

# Create tools
wikipedia_tool = Tool(
    name="Wikipedia Search",
    func=wikipedia.run,
    description="Useful for getting information from Wikipedia"
)

duckduckgo_tool = Tool(
    name="DuckDuckGo Search",
    func=search.run,
    description="Useful for general internet searches"
)

researcher = Agent(
    role='Anime Researcher',
    goal='Find accurate information about anime from Wikipedia',
    backstory='An otaku with extensive knowledge of anime and expert research skills.',
    tools=[wikipedia_tool, duckduckgo_tool],
    llm=llm,
    verbose=True
)

explainer = Agent(
    role='Anime Explainer',
    goal='Provide clear and concise explanations of anime',
    backstory='A passionate anime critic and educator who can break down complex anime concepts for anyone.',
    tools=[wikipedia_tool, duckduckgo_tool],
    llm=llm,
    verbose=True
)