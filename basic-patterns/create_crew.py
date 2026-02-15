from crewai import Crew, Agent, Task

# Define the agent
agent = Agent(
    name="Example Agent",
    role="Researcher",
    goal="Find relevant information",
    backstory="Expert in web research",
    llm="openai/gpt-4o-mini"  # Just use model string
)

# Define the task
task = Task(
    description="Research Python packages for automation",
    agent=agent,
    expected_output="A list of recommended Python packages for automation."
)

# Create the crew
crew = Crew(
    agents=[agent],
    tasks=[task]
)

# Run the crew
result = crew.kickoff()
print(result)


