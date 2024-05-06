from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
import os

# Initialize the LLM with API credentials
llm = ChatGroq(
    model="llama3-8b-8192",
    api_key="YOUR_API_KEY_HERE"
)

# Create an instance of the DuckDuckGoSearchRun tool for search capabilities
search_tool = DuckDuckGoSearchRun()

# Get user input for the query
input_query = input("What is your query for the software design specification? ")

# Configure the Software Architect agent
software_architect_agent = Agent(
    role="Software Architect",
    goal="Develop a detailed software design specification",
    backstory="Experienced in designing scalable and robust systems",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Task for the Software Architect
software_architect_task = Task(
    description=input_query,
    expected_output="A detailed software design specification with tech stack, API descriptions, data objects, and data flow diagrams.",
    agent=software_architect_agent
)

# Configure the Senior Developer agent
senior_developer_agent = Agent(
    role="Senior Developer",
    goal="Elaborate on the software architecture and tech stack",
    backstory="Expert in developing high-performance applications and selecting appropriate technologies.",
    allow_delegation=True,
    verbose=True,
    tools=[search_tool],
    llm=llm
)

# Task for the Senior Developer
senior_developer_task = Task(
    description="Provide a detailed report on the tech stack, APIs, and data flow planning based on the software design specification.",
    expected_output="A comprehensive report including tech stack recommendations, API specs, and data flow diagrams.",
    agent=senior_developer_agent
)

# Configure the Editor agent
editor_agent = Agent(
    role="Editor",
    goal="Compile, format, and present the final document in Markdown",
    backstory="Skilled in editing and presenting technical documentation clearly and effectively.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Task for the Editor
editor_task = Task(
    description="Compile and format the outputs from all agents into a unified Markdown document.",
    expected_output="A well-formatted and cohesive Markdown document that includes all resources and findings.",
    agent=editor_agent
)

# Define the crew and the process
crew = Crew(
    agents=[software_architect_agent, senior_developer_agent, editor_agent],
    tasks=[software_architect_task, senior_developer_task, editor_task],
    process=Process.sequential,
    verbose=2
)

# Execute the crew process
result = crew.kickoff()

# Print the result
print(result)
