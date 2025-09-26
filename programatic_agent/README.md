# Programatic Agent

A cryptocurrency symbol agent that demonstrates Google ADK's programmatic API usage with structured output schemas, designed for agent-to-agent communication in production environments.

## Example Prompt

```
What is the trading symbol for Ethereum?
```

## Setup Instructions

### 1. Create Environment File

Create a `.env` file in the project root with the following variables:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
MODEL=gemini-2.5-flash
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
export MODEL=gemini-2.5-flash
python3 app_agent/agent.py
```

## Agent Capabilities

This agent can:
- Answer cryptocurrency trading symbol questions with structured JSON output
- Demonstrate programmatic ADK usage patterns for production environments
- Show structured output schema implementation using Pydantic models
- Log queries and responses through custom callbacks

The agent uses the Gemini 2.5 Flash model with an InMemoryRunner and includes:
- **Output Schema**: Uses Pydantic `CryptoInfo` model to return structured JSON responses with a `symbol` field
- **Transfer Restrictions**: Configured with `disallow_transfer_to_parent=True` and `disallow_transfer_to_peers=True` as required when using output schemas
- **Custom Logging**: Includes callback functions for debugging and monitoring agent interactions

This setup is ideal for agent-to-agent communication in production systems where structured, predictable output formats are required.