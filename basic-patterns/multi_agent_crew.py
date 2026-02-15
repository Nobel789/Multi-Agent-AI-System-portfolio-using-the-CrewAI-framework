from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define agents
researcher = Agent(
    name="Researcher",
    role="Web Research Specialist",
    goal="Find the latest trends in AI automation",
    backstory="An expert at scouting the internet for fresh insights.",
    llm="openai/gpt-4o-mini"
)

writer = Agent(
    name="Writer",
    role="Technical Writer",
    goal="Summarize research into readable articles",
    backstory="A skilled writer who makes complex info clear.",
    llm="openai/gpt-4o-mini"
)

# Define tasks
research_task = Task(
    description="Research and list the top 3 trends in AI automation.",
    agent=researcher,
    expected_output="A bullet-point list of three AI automation trends."
)

writing_task = Task(
    description="Write a short article (100 words) summarizing these trends for a tech audience.",
    agent=writer,
    expected_output="A concise, engaging article about AI automation trends."
)

# Create crew and run
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task]
)

# This line must be at the top level
result = crew.kickoff()
print(result)

