from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv




# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")







# Web Search Agent: Searches the web for information
web_search_agent = Agent(
    name="Web Search Agent",  # Name of the agent
    role="Search the web for the information",  # Role description
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),  # Using Groq Llama3 model
    tools=[DuckDuckGo()],  # Uses DuckDuckGo for web searches
    instructions=["Always include sources"],  # Ensures sources are always included
    show_tools_calls=True,  # Display tool usage logs
    markdown=True,  # Format responses in Markdown
)









# Financial Agent: Provides stock market insights
finance_agent = Agent(
    name="Finance AI Agent",  # Name of the agent
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),  # Using Groq Llama3 model
    tools=[
        YFinanceTools(
            stock_price=True,  # Fetches stock prices
            analyst_recommendations=True,  # Includes analyst recommendations
            stock_fundamentals=True,  # Provides stock fundamentals
            company_news=True,  # Retrieves latest company news
        ),
    ],
    instructions=["Use tables to display the data"],  # Display financial data in table format
    show_tool_calls=True,  # Display tool usage logs
    markdown=True,  # Format responses in Markdown
)




# Multi-Agent System: Combines both Web Search and Financial Agents
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],  # Teaming up both agents
    instructions=["Always include sources", "Use tables to display the data"],  # Combined agent instructions
    show_tool_calls=True,  # Display tool usage logs
    markdown=True,  # Format responses in Markdown
)

# Querying the Multi-Agent system for financial insights
multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA", 
    stream=True  # Enable streaming for real-time response
)
