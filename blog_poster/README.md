# Blog Poster Agent

A journaling assistant that helps users maintain good daily journaling habits by creating and managing journal entries.

## Example Prompt

```
How is your day going? I'd like to write a journal entry about it.
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
- Help users reflect on their day
- Create dated journal entries in text format
- Append to existing journal entries
- Manage daily journaling habits

The agent uses the Gemini 2.0 Flash model and includes tools for date retrieval and journal entry writing.