# Wiki Agent

A research agent that answers questions by querying Wikipedia using LangChain tools to provide comprehensive, fact-based information on various topics.

## Example Prompt

```
Can you research the history and cultural impact of the Renaissance period in Europe?
```

## Setup Instructions

### 1. Create Environment File

Create a `.env` file in the project root with the following variables:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
MODEL=gemini-2.0-flash
```

Replace `your_api_key_here` with your actual Google API key.

### 2. Set Up Python Virtual Environment

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install google-adk
pip install -r requirements.txt
```

### 4. Run the Project

Unlike other ADK projects, this agent is run directly via command line:

```bash
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY=your_api_key_here
export MODEL=gemini-2.0-flash
python3 langchain_tool_agent/agent.py
```

## Agent Capabilities

This agent can:
- Research topics using Wikipedia's comprehensive database
- Provide detailed information on historical events, people, and concepts
- Answer questions with fact-based responses from reliable sources
- Process complex research queries and deliver structured information

The agent uses the Gemini 2.0 Flash model with LangChain's WikipediaQueryRun tool and includes:
- **Wikipedia Integration**: Uses LangChain's WikipediaQueryRun tool with WikipediaAPIWrapper for comprehensive research
- **Custom Logging**: Includes callback functions for debugging and monitoring agent interactions
- **Structured Research**: Designed to handle complex research queries and provide detailed, factual responses

This setup is ideal for educational research, fact-checking, and comprehensive topic exploration.