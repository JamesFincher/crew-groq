# from crewai import Agent, Task, Crew, Process
# from langchain_groq import ChatGroq
# from langchain_community.tools import DuckDuckGoSearchRun

# import os

# # Instantiate the language model with API key
# llm = ChatGroq(
#     model="llama3-8b-8192",
#     api_key="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")

# # Create an instance of the DuckDuckGoSearchRun tool
# search_tool = DuckDuckGoSearchRun()

# # Get user input for the query
# input_query = input("What is your query? ")

# # Configure junior analyst agent
# junior_analyst_agent = Agent(role="Junior Stock Analyst",
#                              goal="Find best New Stocks and provide quick report",
#                              backstory="You are an excellent junior stock market analyst",
#                              allow_delegation=False,
#                              verbose=True,
#                              llm=llm)

# # Task for the junior analyst agent
# junior_analyst_task = Task(description=input_query,
#                            expected_output="",
#                            agent=junior_analyst_agent)

# # Configure senior analyst agent
# analyst_agent = Agent(role="Senior Stock Analyst",
#                       goal="To provide a detailed report to the customer on any stocks based on today's market situation",
#                       backstory="You are an excellent stock market analyst and Financial expert. Known as the best research analyst, you're skilled in sifting through news, company announcements, stock price and market sentiments. Use right tickers for each stock.",
#                       allow_delegation=False,
#                       verbose=True,
#                       tools=[search_tool],
#                       llm=llm)

# # Task for the senior analyst agent
# agent_task = Task(description="Do a detail analysis of stocks provided by the junior stock analyst",
#                   expected_output="A Full report based on their Current Price, Profit, Market Sentiment and their Research or Investment Plans. Generate this report based on the live analysis of this month data of those stocks. Install python libraries if needed and use internet if required.",
#                   agent=analyst_agent)

# # Define the crew and process
# crew = Crew(
#     agents=[junior_analyst_agent, analyst_agent],
#     tasks=[junior_analyst_task, agent_task],
#     process=Process.sequential,
#     verbose=2
# )

# # Execute the crew process
# result = crew.kickoff()

# # Print the result
# print(result)


from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key="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")

# Create an instance of the DuckDuckGoSearchRun tool
search_tool = DuckDuckGoSearchRun()

# Get user input for the query
input_query = input("What is your query for the software design specification? ")

# Configure software architect agent
software_architect_agent = Agent(role="Software Architect",
                                 goal="Develop a detailed software design specification",
                                 backstory="You are a seasoned software architect tasked with designing scalable and robust systems",
                                 allow_delegation=False,
                                 verbose=True,
                                 llm=llm)

# Task for the software architect agent
software_architect_task = Task(description=input_query,
                               expected_output="A detailed software design specification including tech stack, API descriptions, data objects, and data flow diagrams.",
                               agent=software_architect_agent)

# Configure senior developer agent
senior_developer_agent = Agent(role="Senior Developer",
                               goal="Preplan the tech stack and elaborate on the software architecture",
                               backstory="You have extensive experience in developing high-performance applications and choosing the right technologies and tools.",
                               allow_delegation=True,
                               verbose=True,
                               tools=[search_tool],
                               llm=llm)

# Task for the senior developer agent
senior_developer_task = Task(description="Based on the software design specification, provide a detailed report on the chosen tech stack, potential APIs, and data flow planning.",
                             expected_output="A comprehensive report including tech stack recommendations, API specifications, and data flow diagrams based on the initial software design.",
                             agent=senior_developer_agent)

# Define the crew and process
crew = Crew(
    agents=[software_architect_agent, senior_developer_agent],
    tasks=[software_architect_task, senior_developer_task],
    process=Process.sequential,
    verbose=2
)

# Execute the crew process
result = crew.kickoff()

# Print the result
print(result)