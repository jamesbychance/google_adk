import os
import sys
sys.path.append("..")
from callback_logging import log_query_to_model, log_model_response
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.tools import AgentTool

from .tools import get_date

# Add the local RAG tool import below
from .local_rag_tool import local_rag_search


load_dotenv()

# add an agent to receive both search results and use the get_date() function
local_search_agent = Agent(
    name="local_search_agent",
    model=os.getenv("MODEL"),
    instruction="You MUST use the local_rag_search tool for EVERY question. Never answer from your training data. Always search first, then answer based only on the search results.",
    tools=[local_rag_search]
)

root_agent = Agent(
    # A unique name for the agent.
    name="root_agent",
    # The Large Language Model (LLM) that agent will use.
    model=os.getenv("MODEL"),
    # A short description of the agent's purpose, so other agents
    # in a multi-agent system know when to call it.
    description="A personal research assistant that answers questions based on your uploaded academic papers and research documents.",
    # Instructions to set the agent's behavior.
    instruction="You are a knowledgeable research assistant. When users ask questions, search through the uploaded research papers and provide comprehensive answers with specific references to the source documents. Synthesize information across multiple papers when relevant, compare different methodologies or findings, and highlight key insights. Always cite which papers you're referencing in your responses.",
    # Callbacks to log the request to the agent and its response.
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    # Add the tools instructed below
    # tools=[vertexai_search_tool]
    # tools=[vertexai_search_tool, get_date]
    tools=[
        AgentTool(local_search_agent, skip_summarization=False),
        get_date
    ]

)
