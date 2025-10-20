# Website Scraper Agent

A web scraping agent that uses CrewAI tools to extract and analyze content from websites, specifically designed to scrape the latest news from YC Hacker News.

## Example Prompt

```
Can you scrape the latest news from Hacker News and tell me what the top stories are about?
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
python3 web_scrape/agent.py
```

## Agent Capabilities

This agent can:
- Scrape website content using CrewAI tools
- Extract and analyze the latest news from YC Hacker News
- Process web content for analysis and summarization
- Log queries and responses through custom callbacks

The agent uses the Gemini 2.0 Flash model with CrewAI's ScrapeWebsiteTool and includes:
- **Web Scraping**: Uses CrewAI's ScrapeWebsiteTool to extract content from websites
- **Custom Logging**: Includes callback functions for debugging and monitoring agent interactions
- **Structured Processing**: Designed to handle and analyze scraped web content efficiently

This setup is ideal for automated web content extraction and analysis tasks.