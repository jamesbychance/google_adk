# Google Search Agent

A research agent that answers questions by performing Google searches and analyzing the search results to provide fact-based responses.

## Example Prompt

```
What are the latest developments in quantum computing research in 2024?
```

## Setup Instructions

### 1. Create Environment File

Create a `.env` file in the project root with the following variables:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
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
```

### 4. Run the Project

You can start this project using Google ADK in two ways:

#### Terminal
```bash
adk run
```

#### Web Interface
```bash
adk web
```

## Agent Capabilities

This agent can answer questions about:
- Current events and news
- Research topics and developments
- General knowledge queries requiring up-to-date information

The agent uses the Gemini 2.0 Flash model and includes the Google Search tool for comprehensive information retrieval.