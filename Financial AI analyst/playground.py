import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq
import os
import phi
from phi.playground import Playground, serve_playground_app

# Load environment variables from .env file
load_dotenv()

# Set PHI API key from environment variables
phi.api = os.getenv("PHI_API_KEY")

# Web Search Agent: Responsible for searching the web and retrieving information
web_search_agent = Agent(
    name="Web Search Agent",  # Name of the agent
    role="Search the web for the information",  # Description of its role
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),  # Using Groq Llama3 model
    tools=[DuckDuckGo()],  # Using DuckDuckGo for web search
    instructions=["Always include sources"],  # Ensuring sources are always included
    show_tools_calls=True,  # Show tool usage logs
    markdown=True,  # Format responses in Markdown
)

# Financial Agent: Fetches financial data and provides insights
finance_agent = Agent(
    name="Finance AI Agent",  # Name of the agent
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),  # Using Groq Llama3 model
    tools=[
        YFinanceTools(
            stock_price=True,  # Fetches stock prices
            analyst_recommendations=True,  # Includes analyst recommendations
            stock_fundamentals=True,  # Provides stock fundamentals
            company_news=True,  # Fetches latest company news
        ),
    ],
    instructions=["Use tables to display the data"],  # Format responses in table format
    show_tool_calls=True,  # Show tool usage logs
    markdown=True,  # Format responses in Markdown
)

# Create a Playground app with the defined agents
app = Playground(agents=[finance_agent, web_search_agent]).get_app()

# Run the Playground app when the script is executed
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)  # Starts the app with live reloading
