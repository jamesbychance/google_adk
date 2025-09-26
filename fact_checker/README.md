# Fact Checker Agent

An intelligent fact-checking system that verifies and refines LLM-generated answers by cross-referencing information with web search results.

## Example Prompt

```
Is it true that the Great Wall of China is visible from space? Please verify this claim and provide accurate information.
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

This agent can:
- Evaluate LLM-generated answers for accuracy
- Verify information using web search
- Refine responses to ensure alignment with real-world knowledge

The agent uses the Gemini 2.0 Flash model and includes a sequential workflow with critic and reviser sub-agents for comprehensive fact-checking.